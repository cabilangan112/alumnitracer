from django.urls import path

from .views import (
        AlumniAdminView,
        AlumniAdminDetailView,
        PersonalInfoCreateView,
    )
app_name='alutracer'

urlpatterns = [
    path('list/', AlumniAdminView.as_view(), name='alumni-list'),
    path('alumni/<int:pk>/', AlumniAdminDetailView.as_view(), name='alumni-detail'),
    path('create/<email>/', PersonalInfoCreateView.as_view(), name='personal-form'),
 
 
] 