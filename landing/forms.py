from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
   class Meta:
       model = Application
       fields = ['client_name', 'client_last_name', 'client_phone_number']

