from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User



# 01553280608 - zarif khondokar

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account has been created')
            return redirect('wallophob_home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)

def profile(request):

    user = request.user

    context = {
        'user': user,
    }

    return render(request, 'users/profile.html', context)




