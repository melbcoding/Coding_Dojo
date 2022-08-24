from django.shortcuts import render, redirect
from .models import Books, Authors

def index(request):
    context = {
        "all_books": Books.objects.all()
    }
    return render(request, "Books.html", context)