from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registrationview,logout_views


urlpatterns = [
    path('login/',obtain_auth_token, name='login'),
    path('register/',registrationview,name = 'register'),
    path('logout/',logout_views,name = 'register'),
  
]