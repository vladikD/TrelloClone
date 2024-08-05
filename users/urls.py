from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView, CustomTokenRefreshView, GitHubLogin, GoogleLogin

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('github/', GitHubLogin.as_view(), name='github_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
