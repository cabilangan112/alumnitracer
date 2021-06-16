from django.urls import path

from .views import (
        AlumniAdminView,
        AlumniAdminDetailView,
        PersonalInfoCreateView,
        EditformView
    )
app_name='alumni'

urlpatterns = [
    path('list/', AlumniAdminView.as_view(), name='alumni-list'),
    path('alumni/<int:pk>/', AlumniAdminDetailView.as_view(), name='alumni-detail'),
    path('create/<email>/', PersonalInfoCreateView.as_view(), name='personal-form'),
    path('Editform/<user>/', EditformView, name='edit-form'),
] 