from django import forms
from .models import Books

class BooksCreateForm(forms.ModelForm):
    name = forms.CharField(label="Kitob nomi")
    book = forms.FileField()

