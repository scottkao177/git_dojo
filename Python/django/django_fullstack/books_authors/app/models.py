from django.db import models

# Create your models here.

# remember to always:
# python manage.py makemigrations
# python manage.py migrate
# when making any changes in model.py! Think of it as saving.

# Start up Django shell to enable CRUD commands:
# python manage.py shell
# from app_name.models import class1, class2, etc... (In this instance Author, Book)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Insert Many to many relationship(Must not be the first class in models!)
    # related_name must be plural books, authors, etc.
    books = models.ManyToManyField(Book, related_name='authors')
    notes = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

# Creating objects (in this instance new authors & books)
# insert_author_name = Author.objects.create(first_name="insert first name", last_name="insert last name")
# insert_book_name = Book.objects.create(title="insert name here", description="insert description about book here")

# Adding author id and book id (order matters!)
# insert author_name.books.add(book_name)
# note: author is the related name within the key "books" in class Author

# Display current book/author objects
# insert_author_name.books.all()
# insert_book_name.authors.all()