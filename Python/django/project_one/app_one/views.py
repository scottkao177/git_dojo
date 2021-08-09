# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def hello_name(request, name):
    context = {
        "htmlname": name
    }
    return render(request, "helloname.html", context)
# def create(request):
#     return redirect("/app-one")

# def show(request, num):
#     return HttpResponse(f"placeholder to display blog number:{num}")

# def edit(request, num):
#     return HttpResponse(f"placeholder to edit blog {num}")

# def destroy(request, num):
#     return redirect("")