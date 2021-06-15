from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalInformation
from account.decorators import user_required, staff_required
from .forms import PersonalInformationForm
# Create your views here.



class AlumniAdminView(LoginRequiredMixin, View):
    def get(self, request,*args, **kwargs):
        query = self.request.GET.get('q')
        qs = PersonalInformation.objects.all().order_by("-date_modified").search(query)

        if qs.exists():
            return render(request, "alumni/alumni_list.html",{'qs':qs,})
        return render(request, "alumni/alumni_list.html",{'qs':qs,})
 
class AlumniAdminDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        alumni = get_object_or_404(PersonalInformation, pk=pk)
        context = {
            'alumni':alumni
        }
        return render(request, 'alumni/alumni_detail.html', context)

 
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
                     