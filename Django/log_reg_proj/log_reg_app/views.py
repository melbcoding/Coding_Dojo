from django.shortcuts import render, redirect
from .forms import RegisterForm

def index(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, 'index.html', context)