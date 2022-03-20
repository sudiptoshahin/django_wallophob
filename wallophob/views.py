from django.shortcuts import render
from django.http.response import HttpResponse



def wallophob(request):

    context = {
        'title': 'Home'
    }
    return render(request, 'wallophob/home.html', context)


