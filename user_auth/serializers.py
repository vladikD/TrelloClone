from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import re

User = get_user_model()
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username вже використовується.")

        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise serializers.ValidationError("Username може містити лише букви, цифри і символи _.")

        return username

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email вже використовується.")
        return email

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Пароль повинен містити щонайменше 8 символів.")
        if not re.search(r'\d', password):
            raise serializers.ValidationError("Пароль повинен містити хоча б одну цифру.")
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError("Пароль повинен містити хоча б одну велику літеру.")
        return password

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.validated_data
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])
        user.save()
        setup_user_email(request, user, [])
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid login credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def save(self, **kwargs):
        return self.get_token(self.validated_data['user'])



