from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile



# user register form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    contact_no = forms.CharField()
    present_address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'contact_no', 'present_address']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    contact_not = forms.CharField()
    present_address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_no', 'present_address']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']