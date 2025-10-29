from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # signup page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update/<int:pk>/', views.update_kit, name='update_kit'),
    path('postmortem/new/', views.create_postmortem, name='create_postmortem'),
    path('kit/<int:kit_id>/', views.view_kit, name='view_kit'),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('toggle-restock/<int:kit_id>/', views.toggle_restock, name='toggle_restock'),
    path('save-restock-status/<int:kit_id>/', views.save_restock_status, name='save_restock_status'),

]
