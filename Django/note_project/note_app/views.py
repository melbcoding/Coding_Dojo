from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . models import *

def index(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            return redirect('/thewall')
    return render(request, 'welcome.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['userid'] = new_user.id
        return redirect('/dashboard')

def dashboard(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            context = {
                "user": user[0],
                "get_all_notes": Note.objects.all()
            }
        return render(request, 'dashboard.html', context)
    return redirect('/')


def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email_address'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email_address=request.POST['email_address'])
    request.session['userid'] = user.id
    return redirect('/dashboard')

def create(request):
    if request.method =="POST":
            # user = User.objects.get(id)
            Note.objects.create(
                note=request.POST['note'],
                # poster = user
                )
    return redirect('/')

def delete(request):
    note_to_delete = Note.objects.get(id=id)
    note_to_delete.delete()
    return redirect('/')

def logoff(request):
    request.session.flush()
    return redirect('/')