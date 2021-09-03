from Courses.urls import path
from Course_App import views

urlpatterns = [
    path('', views.index),
    path('course', views.index),
    path('course/post', views.post_course),
    path('course/<int:course_id>/get', views.grab_course),
    path('course/<int:course_id>/delete', views.delete_course)
]
