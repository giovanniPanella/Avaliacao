from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.register_user),
    path('users/track/<str:track>/', views.list_users),
    path('status/<str:cpf>/', views.user_status),
]