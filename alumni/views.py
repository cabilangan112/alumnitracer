from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalInformation
 
from .forms import PersonalInformationForm
# Create your views here.

class AlumniAdminView(View):
    def get(self, request,*args, **kwargs):
        query = self.request.GET.get('q')
        qs = PersonalInformation.objects.all().order_by("date_modified").search(query)

        if qs.exists():
            return render(request, "alumni/alumni_list.html",{'qs':qs,})
        return render(request, "alumni/alumni_list.html",{'qs':qs,})
                
 
class AlumniAdminDetailView(View):
    def get(self, request, email, *args, **kwargs):
        personal_info_detail = get_object_or_404(PersonalInformation, email=email)
        context = {
            'personal_info_detail':personal_info_detail
        }
        return render(request, 'alumni/alumni-detail.html', context)

 
class PersonalInfoCreateView(TemplateView):
    """
    Display register in page where registered users can log in
    """   
    template_name = 'registration/alumni_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PersonalInfoCreateView,self).get_context_data(*args, **kwargs)
        title = "register"
        form =PersonalInformationForm(self.request.POST or None,
                                self.request.FILES or None)
        context.update({
            "title":title,
            "form":form,
        })
        return context

    def post(self, user, *args, **kwargs):
        context = self.get_context_data()
        form = context.get('form')
        if form.is_valid():
            user = form.save()
            return redirect('/')
        return render(self.request, self.template_name, context)
                     