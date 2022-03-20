from django.shortcuts import render
from users.forms import UserRegisterForm


def register(request):
    

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

    else:
        form = UserRegisterForm()


    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)
