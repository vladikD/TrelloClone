from django.contrib import admin
from django.urls import path, include
from user_auth.views import home_page


urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('api/user_auth/', include('user_auth.urls')),
    path('accounts/', include('allauth.urls')),

]

