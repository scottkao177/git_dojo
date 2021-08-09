from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

# remember to always:
# python manage.py makemigrations
# python manage.py migrate
# when making any changes in model.py! Think of it as saving.

# Start up Django shell to enable MySQL commands:
# python manage.py shell
# from app_name.models import *

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # One to many relationship: Dojo -> Ninja
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

