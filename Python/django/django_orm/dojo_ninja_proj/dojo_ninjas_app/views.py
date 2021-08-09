from django.shortcuts import render, redirect
from dojo_ninjas_app.models import Dojo, Ninja
# Create your views here.
def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def dojo(request):
    Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        # created_at = request.POST['created_at'],
        # updated_at = request.POST['updated_at'],
    )
    return redirect('/')
    
def ninja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id = request.POST['dojo'],
        # created_at = request.post['created_at'],
        # updated_at = request.post['updated_at'],
    )
    return redirect('/')

