from django.urls import path

from .views import (
 
        PersonalInfoCreateView,
        EditformView
    )
app_name='alumni'

urlpatterns = [
    path('create/<email>/', PersonalInfoCreateView.as_view(), name='personal-form'),
    path('create/', PersonalInfoCreateView.as_view(), name='create-form'),

    path('Editform/<user>/', EditformView, name='edit-form'),
] 