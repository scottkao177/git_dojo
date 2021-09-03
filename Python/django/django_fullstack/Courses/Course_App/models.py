from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)