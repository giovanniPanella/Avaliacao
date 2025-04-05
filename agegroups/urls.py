from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_age_group),
    path('delete/', views.remove_age_group),
    path('list/', views.get_age_groups),
]