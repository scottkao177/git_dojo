from django.db import models
import re
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name requires atleast 3 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name requires atleast 3 characters"
        if len(postData['pw']) < 8:
            errors['pw'] = "password requires atleast 8 characters"
        if postData['pw'] != postData['con_pw']:
            errors['match'] = 'Passwords do not match'
        if not email_regex.match(postData['email']):
            errors['email'] = ('invalid email address!')
        # one email for one account
        try:
            user = User.objects.get(email = postData['email'])
            errors['email_in_use'] = 'This email is already associated with an account.'
        except:
            pass
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email = postData['email'])
        print(existing_users)
        if len(postData['email'])== 0:
            errors['email'] = ('Requires email address!')
        elif len(existing_users)== 0:
            errors['not_found'] = "Please enter a valid email and password!"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be atleast 8 characters!"
        elif not bcrypt.checkpw(postData['pw'].encode(), existing_users[0].pw.encode()):
            errors['mismatch'] = 'Please enter a valid email and password!'
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
                errors['title'] = 'Please fill out the title.'
        if len(postData['description']) < 5:
                errors['description'] = 'Please write a description for the book. Must be 5 characters long.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #one to many - User who uploaded a given book
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded', on_delete = models.CASCADE)
    #many to many - list of users who favorited a given book
    favorited_by = models.ManyToManyField(User, related_name="fav_books")
    objects = BookManager()

def __str__(self):
    return self.first_name
