from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# user register form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    contact_no = forms.CharField()
    present_address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'contact_no', 'present_address']

