from django.urls import path

from . import views
app_name = 'post'
urlpatterns = [
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.comment, name='post-comment'),
    path('<title>/', views.post_edit, name='post-edit'),    
    path('draft/', views.Draft, name='draft'),
    path('hidden/', views.Hidden, name='hidden'),
    path('add/post/', views.PostCreate, name='add-post'), 
]