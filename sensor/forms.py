from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from web.models import *
from django.contrib.auth import authenticate

class AccountAuthenticationForms(forms.ModelForm):
    password = forms.CharField(label="password" )

    class Meta:
        model = Signup
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")