from django.shortcuts import render,redirect
from myapp.models import Restaurant
from myapp.forms import Restaurant_registration_form,Restaurant_login_form
from django.views.generic import CreateView,FormView
from django.urls import  reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate , login




# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def menu(request):
    return render(request,'menu.html')
def review(request):
    return render(request,'review.html')
def downloadapp(request):
    return render(request,'downloadapp.html')





class RegistrationView(CreateView):
    model = Restaurant
    form_class = Restaurant_registration_form
    template_name = "registration.html"
    success_url = reverse_lazy("signin")


    def form_valid(self,form):
        messages.success(self.request,"account created successfully")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed to create your accound")
        return super().form_invalid(form)


class LoginView(FormView):
    template_name = "login.html"
    form_class = Restaurant_login_form

    def post(self, request, *args, **kwargs):
        form = Restaurant_login_form(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"loged in successfully")
                return redirect("signup")
            else:
                messages.error(request,"login failed")
                return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})


