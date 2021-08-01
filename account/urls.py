from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='post'),
    path('<int:pk>/', views.ProfileDetailView.as_view(), name='detail'),
    path('<user>/', views.UserDetailView.as_view(), name='user-detail'),
    path('upload/<email>/', views.UploadView, name='upload'),
    path('profile/edit/<email>/', views.EditProfileView, name='edit_profile'),
    path('password/edit/<id_number>/', views.EditPassword.as_view(), name='edit_password'),
]