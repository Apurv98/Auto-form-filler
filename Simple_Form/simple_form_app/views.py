from django.shortcuts import render
from django.views import View
from .forms import SimpleForm,CaptchaForm
from .models import FormData
# Create your views here.

class HomeView(View):
    template_name = 'simple_form_app/index.html'
    form = SimpleForm()
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})

    def post(self,request):
        form = SimpleForm(request.POST)
        if form.is_valid():
            form_data = FormData()
            form_data.name = form.cleaned_data['name']
            form_data.department = form.cleaned_data['department']
            form_data.save()
            count = len(FormData.objects.all())
            return render(request,self.template_name,{'form':self.form,'count':count})
        else:
            return render(request,self.template_name,{'form':self.form,'wrong_captcha':True})

class CaptchaView(View):
    template_name = 'simple_form_app/index.html'
    form = CaptchaForm()
    def get(self,request):
        return render(request,self.template_name,{'form':self.form})

    def post(self,request):
        form = CaptchaForm(request.POST)
        if form.is_valid():
            form_data = FormData()
            form_data.name = form.cleaned_data['name']
            form_data.department = form.cleaned_data['department']
            form_data.save()
            count = len(FormData.objects.all())
            return render(request,self.template_name,{'form':self.form,'count':count})
        else:
            return render(request,self.template_name,{'form':self.form,'wrong_captcha':True})
