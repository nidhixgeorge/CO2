from types import MethodWrapperType
from django import forms
from django.db.models.fields import DateField, EmailField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import SelectDateWidget
from django.forms.widgets import Select, Textarea

class CarbonForm1(forms.Form):
    start_point = forms.CharField(label='Start', max_length = 50)
    address_line1 = forms.CharField(label='Address Line 1', max_length = 50)
    address_line2 = forms.CharField(label='Address Line 2', max_length = 50)
    city = forms.CharField(label='City', max_length = 50)
    state = forms.CharField(label='State', max_length = 50)
    zipcode = forms.CharField(label='Zip', max_length = 20)

class CarbonForm2(forms.Form):
    end_point = forms.CharField(label='End Location', max_length = 50)
    address_line1 = forms.CharField(label='Address Line 1', max_length = 50)
    address_line2 = forms.CharField(label='Address Line 2', max_length = 50)
    city = forms.CharField(label='City', max_length = 50)
    state = forms.CharField(label='State', max_length = 50)
    zipcode = forms.CharField(label='Zip', max_length = 20)


