"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import  path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from account.views import LoginView, RegisterView,password_reset_request 
from post.views import PostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='post'),
    path('login', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    path('account/', include('account.urls', namespace='user')),
    path('alumni/', include('alumni.urls', namespace='alumni')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('post/', include('post.urls', namespace='post')),
    path('register/',RegisterView.as_view(), name='register'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
  
    path('reset_password/', auth_views.PasswordResetView.as_view(), name ='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),  

]
urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
 