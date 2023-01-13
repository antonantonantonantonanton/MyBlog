"""It defines URL schemas for users"""
from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    # enable default URL authorization.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
