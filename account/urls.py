from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='post'),
 
    path('<user>/', views.ProfileDetailView.as_view(), name='detail'),
    path('profile/edit/<email>/', views.EditProfileView, name='edit_profile'),
    path('password/edit/<id_number>/', views.EditPassword.as_view(), name='edit_password'),
]