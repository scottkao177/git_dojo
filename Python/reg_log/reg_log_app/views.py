from django.shortcuts import render, redirect
from reg_log_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    request.session.flush()
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def post_register(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt(14)).decode()

    #create new user in db
    create_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        pw = hashed_pw,
    )
    #store user id in request.session
    request.session['user_id'] = create_user.id
    return redirect('/main/success')

def post_login(request):
    if request.method != "POST":
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    #user that is loggin in
    this_user = User.objects.filter(email = request.POST['email'])[0]
    request.session['user_id'] = this_user.id
    messages.success(request, "Your logged in!")
    return redirect('/main/success')


def post_logout(request):
    request.session.flush()
    return redirect('/')

def success_page(request):
    #only registered users can access this page
    if 'user_id' not in request.session:
        messages.error(request, "Must be logged in to view page!")
        return redirect('/')
    
    else:
        context = {
            'this_user': User.objects.get(id = request.session['user_id'])
        }
    return render(request, 'success.html', context)
