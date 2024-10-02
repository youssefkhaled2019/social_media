from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    class Meta :
        model=User
        fields=["username" ,"email","password1","password2"]
        # extra_kwargs = {'email': {'required': True}}



class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField() # required
    class Meta:
        model=User
        fields=["username","email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["image"] 