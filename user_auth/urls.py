from django.urls import path
from .views import RegisterView, LoginView, CustomTokenObtainPairView, CustomTokenRefreshView, GitHubLogin, GoogleLogin

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('github/', GitHubLogin.as_view(), name='github_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
]