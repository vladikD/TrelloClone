from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterSerializer, LoginSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request)
            return Response({"detail": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.save()
            return Response(token, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (permissions.AllowAny,)

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


def home_page(request):
    return render(request, 'home.html')


