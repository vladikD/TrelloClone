from django.contrib import admin
from django.urls import path, include
from users.views import home_page


urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

]

