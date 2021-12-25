from django.shortcuts import render
from django.views.generic.base import TemplateView,View
from django.shortcuts import get_object_or_404, redirect
from .models import Course,Department
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from alumni.models import PersonalInformation
from django.views import generic
from.models import User
from django.urls import reverse	
from .forms import UserLoginForm,UploadForm, PasswordResetForm,UserRegisterForm,EditProfileForm,EditPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
 
class ProfileView(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        query = self.request.GET.get('q')
        qs = PersonalInformation.objects.all().order_by("-date_modified").search(query)

        if qs.exists():
            return render(request, "profile/profile_list.html",{'qs':qs})
        return render(request, "profile/profile_list.html",{'qs':qs})

class UserDetailView(LoginRequiredMixin, View):
    def get(self, request, user, *args, **kwargs):
        alumni  = get_object_or_404(PersonalInformation, user=request.user)
        context = {
            'alumni':alumni
        }
        return render(request, "profile/profile_detail.html", context)

class ProfileDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        alumni  = get_object_or_404(PersonalInformation, pk=pk)
        context = {
            'alumni':alumni
        }
        return render(request, "profile/profile_detail.html", context)

class LoginView(TemplateView):
    template_name = "registration/login.html"
 
    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        title = "Login"
        form = UserLoginForm(self.request.POST or None)  
        context.update({
			"title":title,
			"form":form,
		})
        return context

    def post(self,  request, *args, **kwargs):
        context = self.get_context_data()
        form = context.get('form')
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return redirect('post')

        return render(self.request, self.template_name, context)

class DepartmentView(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
        qs = Department.objects.all().order_by("-date_modified") 
        return render(request, "profile/department_list.html",{'qs':qs})

class CourseView(LoginRequiredMixin,View):
    def get(self, request,*args, **kwargs):
 
        qs = Course.objects.all().order_by("-date_modified") 
 
        return render(request, "profile/course_list.html",{'qs':qs})

class RegisterView(TemplateView):
	"""
	Display register in page where registered users can log in
	"""
	template_name = "registration/registration_form.html"

	def get_context_data(self, *args, **kwargs):
		context = super(RegisterView, self).get_context_data(*args, **kwargs)
		title = "register"
		form = UserRegisterForm(self.request.POST or None,
								self.request.FILES or None)
		context.update({
			"title":title,
			"form":form,
		})
		return context

	def post(self, *args, **kwargs):
		context = self.get_context_data()
		form = context.get('form')
		if form.is_valid():
			user = form.save()
			login(self.request, user,backend='django.contrib.auth.backends.ModelBackend')
			return redirect('alumni:personal-form', email=user.email)
		return render(self.request, self.template_name, context)


def  EditProfileView(request, email):
    user = get_object_or_404(User, email=email)
    if request.method == "POST":
        form = EditProfileForm(request.POST or None, instance=user)
        if form.is_valid():           
            user = form.save(commit=False) 
            user.save()
            return redirect('user:user-detail', user=user)
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'profile/profile-edit.html',{'form': form,
        'user':user})


def UploadView(request, email):
    user = get_object_or_404(User, email=email)
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES, instance=user )
        if form.is_valid():           
            user = form.save(commit=False) 
            user.user = request.user
            user.save()
            return redirect('account:post')
    else:
        form = UploadForm(instance=user)
    return render(request, 'profile/upload.html',{'form': form,
        'user':user})


class EditPassword(LoginRequiredMixin, generic.TemplateView):
    """
    Edit the currently logged in user's password
    """    
    login_url = 'login'
    template_name='password-edit.html'

    def get(self, id_number, *args, **kwargs):
        title = 'Edit Password'
        user = self.request.user
        users = User.objects.all()
        instance = get_object_or_404(User, id_number=id_number)

        form = EditPasswordForm(
            self.request.POST or None
        )

        context = {
            'title':title,
            'form':form,
            'prof_instance':instance,
            'users':users,
        }

        return render(self.request, self.template_name, context)

    def post(self,id_number, *args, **kwargs):
        title = 'Edit Password'
        users = User.objects.all()
        user = self.request.user
        instance = get_object_or_404(User, id_number=id_number)

        form = EditPasswordForm(
            self.request.POST or None
        )

        if form.is_valid():
            form.save(user=user)
            login(self.request, user)
            return HttpResponseRedirect(reverse('/'))

        context = {
            'title':title,
            'form':form,
            'prof_instance':instance,
            'users':users,
        }

        return render(self.request, self.template_name, context)

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')
                        
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("/" )
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html", context={"password_reset_form":password_reset_form})