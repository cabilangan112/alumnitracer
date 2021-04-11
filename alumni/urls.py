from django.urls import path

from .views import (
        PersonalInfoDetailView,
        PersonalInfoCreateView
    )
app_name='alutracer'

urlpatterns = [
    path('create/', PersonalInfoCreateView.as_view(), name='personal-info-create'),
    path('<slug:slug>/', PersonalInfoDetailView.as_view(), name='personal-info-detail'),
    # path('course', course_list, name='course-list'),
    # path('choice', choice_list, name='choice-list'),
    # path('personal-information', personal_information_list, name='personal-information-list'),
    # path('question', question_list, name='question-list'),
    # path('course/<str:pk>', course_detail, name='course-detail'),
    # path('choice/<str:pk>', choice_detail, name='choice-detail'),
    # path('personal-information/<str:pk>', personal_information_detail, name='personal-information-detail'),
    # path('question/<str:pk>', question_detail, name='question-detail')
]