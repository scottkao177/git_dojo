from django.shortcuts import render, redirect
from fav_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

# index.html paths
def index(request):
    request.session.flush()
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt(14)).decode()

    # create new user in db
    create_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        pw = hashed_pw,
    )
    # store user id in request.session
    request.session['user_id'] = create_user.id
    return redirect('/success')

def login(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    # user that is loggin in
    this_user = User.objects.filter(email = request.POST['email'])[0]
    request.session['user_id'] = this_user.id
    messages.success(request, "Your logged in!")
    return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')

# dashboard.html + add book + fav/unfav function
def success_dashboard(request):
    # only registered users can access this page
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view page!")
        return redirect('/')

    else:
        this_user = User.objects.get(id = request.session['user_id'])
        all_books = Book.objects.all()
        user_books = Book.objects.filter(uploaded_by = request.session['user_id'])
        context = {
            #shows all books created on site
            'all_books': all_books,
            #get request.session for current User
            'this_user': this_user,
            #count all books by user
            'user_books': user_books.count()
        }
        
    return render(request, 'dashboard.html', context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success')
    else:
        user = User.objects.get(id = request.session['user_id'])
        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            uploaded_by = user
        )
        #automatically favorite book when created
        user.fav_books.add(book)
        return redirect(f'/current/{book.id}/book')

def favorite_book(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.fav_books.add(book)
    return redirect(f'/current/{book_id}/book')

def unfavorite_book(request, book_id):
    user = User.objects.get(id=request.session["user_id"])
    book = Book.objects.get(id=book_id)
    user.fav_books.remove(book)
    return redirect(f'/current/{book_id}/book')

# edit description + delete book
def edit_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.description = request.POST['description']
    book.save()
    return redirect(f'/current/{book_id}/book')

def delete_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return redirect('/success')

# current(book).html
def current_book(request, book_id):
    context = {
        'book': Book.objects.get(id = book_id),
        'this_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'current.html', context)

