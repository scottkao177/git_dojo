from django.shortcuts import render, redirect
from q_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

# index.html paths
def index(request):
    request.session.flush()
    context = {
        'users': User.objects.all()
    }
    return render(request, 'register_login.html', context)

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
        return redirect('/dashboard')
    # This email for logged in user
    this_user = User.objects.filter(email = request.POST['email'])[0]
    request.session['user_id'] = this_user.id
    messages.success(request, "Your logged in!")
    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def success(request):
    # only registered users can access this page
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view page!")
        return redirect('/')
    else:
        context = {
            'this_user': User.objects.get(id = request.session['user_id'])
        }
    return render(request, 'success.html', context)

# dashboard.html + add book + fav/unfav function
def dashboard(request):
    context = {
        'all_quotes': Quote.objects.all(),
        'this_user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'dashboard.html', context)

def add_quote(request):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    else:
        user = User.objects.get(id = request.session['user_id'])
        quote = Quote.objects.create(
            quoter = request.POST['quoter'],
            quote = request.POST['quote'],
            posted_by = user
        )
        #automatically favorite quote when created
        user.favorited_quote.add(quote)
        return redirect(f'/dashboard')

def favorite_quote(request, quote_id):
    user = User.objects.get(id=request.session["user_id"])
    quote = Quote.objects.get(id = quote_id)
    user.favorited_quote.add(quote)
    return redirect('/dashboard')

def unfavorite_quote(request, quote_id):
    user = User.objects.get(id = request.session["user_id"])
    quote = Quote.objects.get(id = quote_id)
    user.favorited_quote.remove(quote)
    return redirect('/dashboard')

# edit description + delete quote
def edit(request, quote_id):
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view page!")
        return redirect('/')
    else:
        context = {
            'quote': Quote.objects.get(id = quote_id)
        }
    return render(request, 'edit.html', context)

def edit_quote(request, quote_id):
    errors = Quote.objects.quote_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{quote_id}')
    else:
        quote = Quote.objects.get(id = quote_id)
        quote.quoter = request.POST['quoter']
        quote.quote = request.POST['quote']
        quote.save()
    messages.success(request, "Quote updated!")
    return redirect(f'/edit/{quote_id}')

def delete_quote(request, quote_id):
    quote = Quote.objects.get(id = quote_id)
    quote.delete()
    return redirect('/dashboard')

# current(quote).html
def quote_poster(request, quote_id):
    poster = Quote.objects.get(id = quote_id)
    all_quotes = Quote.objects.all()
    quote_count = Quote.objects.filter(posted_by = poster.posted_by).count()
    context = {
        'poster': poster,
        'all_quotes': all_quotes,
        'quote_count': quote_count
    }
    return render(request, 'user.html', context)