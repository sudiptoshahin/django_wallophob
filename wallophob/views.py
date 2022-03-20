from django.shortcuts import render
from django.http.response import HttpResponse


def wallophob(request):
    return HttpResponse('<h1>Hello Wallophob</h1>')


