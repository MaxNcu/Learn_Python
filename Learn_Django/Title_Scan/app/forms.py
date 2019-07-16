from django import forms
from ckeditor.fields import RichTextField

username = forms.CharField(label='USERNAME', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
password = forms.CharField(label='PASSWORD', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
email = forms.EmailField(label='EMAIL', widget=forms.TextInput(attrs={'class': 'form-control'}))


class Register(forms.Form):
    username = username
    password = password
    email = email

class Login(forms.Form):
    username = username
    password = password

class Comment(forms.Form):
    comment = RichTextField()
