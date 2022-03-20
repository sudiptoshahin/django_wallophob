from unicodedata import name
from django.urls import path
from wallophob import views


urlpatterns = [
    path('', views.wallophob, name='wallophob-home'),
    path('wallophob/', views.wallophob),


    # about

    # others...
]