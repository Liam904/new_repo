from django.shortcuts import render
from .models import Apointments


def home(request):
    context = {

    }
    return render(request, 'home.html', context)


def appointments(request):
    form = Apointments.objects.all(request.POST)
    context = {
        'form':form
    }
    if request.m
    return render(request, 'appointments.html', context)
