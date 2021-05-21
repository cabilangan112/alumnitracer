from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='post'),

    path('profiles/', views.ProfileAdminView.as_view(), name='profile'),
    path('<email>/', views.ProfileDetailView.as_view(), name='detail'),
    path('profile/edit/<int:pk>/', views.EditProfileView, name='edit_profile'),
    path('password/edit/<id_number>/', views.EditPassword.as_view(), name='edit_password'),
]