from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'form.html')

def form(request):
    if request.method == 'GET':
        return redirect('/')
    #request.session['submitted'] creates persistent data
    #1 name the 'key':
    #2 add request.POST with ['key']
    #3 within {}
    request.session['submitted'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    # redirect to view.submit through redirect to path local.host:8000/result
    return redirect('/result')

def submit(request):
    context = {
        'submitted': request.session['submitted']
    }
    return render(request, 'results.html', context)

# RULE OF THUMB:
# GET request will return a render
# POST request will return a redirect

# Persistent data
# Request.session