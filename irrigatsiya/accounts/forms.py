from django import forms
from .models import Profile, Level, Cafedra, Faculty
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=40)
    # last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    faculty = forms.ChoiceField()
    cafedra = forms.ChoiceField()
    level = forms.ChoiceField()
    class Meta:
        model = User
        fields = ['username', 'email', 'faculty','cafedra','level']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['image']