from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # signup page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<int:pk>/', views.update_kit, name='update_kit'),
    path('postmortem/new/', views.create_postmortem, name='create_postmortem'),
]
