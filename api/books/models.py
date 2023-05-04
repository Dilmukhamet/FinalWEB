from django.db import models
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)

class Book(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.TextField(max_length=255)
    price = models.FloatField(max_length=255, null=False)
    pic = models.CharField(max_length=255)
    genre = models.ForeignKey(to=Genre, on_delete=models.SET_NULL, default=lambda: Genre.objects.get(id=1), related_name="books", null=True)