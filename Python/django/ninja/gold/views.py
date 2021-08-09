from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'main.html')

def duel(request):
    pass

def quest(request):
    pass

def bakuto(request):
    pass

def raid(request):
    pass
    # if request.method == 'GET':
    #     return redirect('/')    # redirect back to main page
    # request.session['outcome'] = {

    # }

def outcome(request):
    pass
    #     context = {
    #     'outcome': request.session['outcome']
    # }
    # return render(request, 'main.html', context)
    # return redirect(request, 'main.html', context)