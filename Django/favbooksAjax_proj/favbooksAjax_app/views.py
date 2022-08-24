from django.shortcuts import render, redirect
from .forms import LoginForm,RegForm,NewBookForm
from .models import *
# from django.contrib import messages
import bcrypt


def logReg(request):
    reg_form = RegForm()
    login_form = LoginForm()
    return render(request, "logReg.html", {'reg_form': reg_form, 'login_form': login_form})

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST, instance=User)
        if reg_form.is_valid():
            reg_form.save()
            print(reg_form.data)
            return redirect('/')
        else:
            return redirect('/')

def login(request):
    # errors = User.objects.login_validator(request.POST)
    # if len(errors):
    #     for key, value in errors.items():
    #         messages.error(request, value)
    #     return redirect('/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            request.session['greeting'] = user.first_name
            return redirect('/main_page')
        else:
            return redirect('/')


def main_page(request):
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
            'form': Book.objects.all(),
            'this_user': User.objects.get(id=request.session['user_id'])
        }
    return render(request, 'main_page.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
    
def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        for e in errors.values():
            messages.error(request, e)
        return redirect('/main_page')
    else:
        user = User.objects.get(id=request.session["user_id"])
        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            creator = user
        )
        return redirect('/main_page')

def books(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'this_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'books.html', context)

def favorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.favorited_books.add(book)
    return redirect('/main_page')


def unfavorite(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.favorited_books.remove(book)

    return redirect('/main_page')

def update(request, book_id):
    book = Book.objects.get(id=book_id)
    book.description = request.POST['description']
    book.save()

    return redirect(f"/books/{book_id}")

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect('/main_page')


