from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalInformation
 
from .forms import PersonalInformationForm
# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        index = Department.objects.all()
        context = {
            'index': index,
 
            'parallax': parallax,
            'thumbnail': thumbnail
        }
        return render(request, 'home.html', context)

class PersonalInfoDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        personal_info_detail = get_object_or_404(PersonalInformation, slug=slug)
        context = {
            'personal_info_detail':personal_info_detail
        }
        return render(request, 'alutracer/alu-detail.html', context)

class PersonalInfoCreateView(View):
    form_class = PersonalInformationForm
    initial = {'key':'value'}
    template_name = 'alutracer/alu-form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            today = date.today()
            dob = post.date_of_birth
            post.age = today.year - dob.year
            if today.month < dob.month or today.month == dob.month and today.day < dob.day:
                post.age -= 1
            post.save()
            return redirect('alutracer:personal-info-detail', slug=post.slug)
        else:
            form = PersonalInformationForm()
        context = {
            'form': form
        }