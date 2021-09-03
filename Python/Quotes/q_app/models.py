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
        if len(postData['pw']) < 8:
            errors['pw'] = 'Password must be 8 characters'
        elif len(postData['email']) == 0:
            errors['email'] = 'Please fill in email'
        elif  len(existing_users) == 0:
            errors['not found'] = 'please fill in email' #valid email
        elif not bcrypt.checkpw(postData['pw'].encode(), existing_users[0].pw.encode()):
            errors['mismatch'] = 'Please enter a valid email and password!'
        return errors

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['quoter']) < 1:
                errors['quoter'] = 'Please add the name of quoter.'
        # elif len(postData['email'])== 0:
        #    errors['quoter not found'] = ('Please add the name of quoter.')
        if len(postData['quote']) < 1:
                errors['quote'] = 'Please type in the quote.'
        # elif len(postData['quote'])== 0:
        #    errors['quote'] = ('Please fill in quote.')
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pw = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Quote(models.Model):
    quoter = models.CharField(max_length=30)
    quote = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #one to many
    posted_by = models.ForeignKey(User, related_name='posted_quote', on_delete = models.CASCADE)
    #many to many
    favorited_by = models.ManyToManyField(User, related_name="favorited_quote")
    objects = QuoteManager()

def __str__(self):
    return self.first_name