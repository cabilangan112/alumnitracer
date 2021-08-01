from datetime import date
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PersonalInformation
from account.decorators import user_required, staff_required
from .forms import PersonalInformationForm,PersonalEditForm
 
 
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
            return redirect('account:post')
        return render(self.request, self.template_name, context)
                     
def  EditformView(request, user):
    prof = get_object_or_404(PersonalInformation, user=request.user)
    if request.method == "POST":
        form = PersonalEditForm(request.POST, instance=prof )
        if form.is_valid():           
            user = form.save(commit=False)
            user.user = request.user
            user.save()
        return redirect("/")
    else:
        form = PersonalEditForm(instance=prof )
    return render(request, 'registration/form-edit.html',{'form': form,'prof':prof})