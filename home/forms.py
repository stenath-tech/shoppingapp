from django import forms 
from django.forms import ModelForm
from . models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'subject', 'email', 'message']


class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']


