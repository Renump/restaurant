from django import forms
from myapp.models import Restaurant


class Restaurant_registration_form(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ["username","password","adress"]


class Restaurant_login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



