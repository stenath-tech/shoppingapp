from django import forms
# from django.contrib.forms import ModelForm
from django.forms import ModelForm
from userprofile.models import *
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField()

    class Meta:
        # Model = User
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')



class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'pix', 'email', 'address', 'phone', 'dob', 'nationality', 'gender', 'state']
        GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),
        ]

        STATE = [
            ('Enugu', 'Enugu'),
            ('Lagos', 'Lagos'),
            ('Delta', 'Delta'),
            ('Abia', 'Abia'),
            ('Akwa-Ibom', 'Akwa-Ibom'),
            ('Imo', 'Imo'),
            ('Ogun', 'Ogun'),
            ('Ekiti', 'Ekiti'),
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Last Name'}),
            'pix': forms.FileInput(attrs={'class': 'forms-control', 'placeholder': 'Profile Image'}),
            'email': forms.EmailInput(attrs={'class': 'forms-control', 'placeholder': 'Email Address'}),
            'address': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Home Address'}),
            'phone': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Phone Number'}),
            'dob': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Date of birth'}),
            'nationality': forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Nationality'}),
            'gender': forms.Select(attrs={'class': 'forms-control', 'placeholder': 'Gender'}, choices= GENDER),
            'state': forms.Select(attrs={'class': 'forms-control', 'placeholder': 'State'}, choices= STATE),
        }

        


