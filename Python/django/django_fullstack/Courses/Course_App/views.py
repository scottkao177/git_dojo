from django.shortcuts import render, redirect
from django.http import HttpResponse
from Course_App.models import Course

# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def post_course(request):
    create_course = Course.objects.create(
        name = request.POST['name'],
        description = request.POST['description']
    )
    return redirect('/')

def grab_course(request, course_id):
    get_course = Course.objects.get(id = course_id)
    context = {
        'this_course': get_course
    }
    return render(request, 'delete.html', context)

def delete_course(request, course_id):
    get_course = Course.objects.get(id = course_id)
    get_course.delete()
    return redirect('/course')
