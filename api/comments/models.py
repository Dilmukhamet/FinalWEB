from django.db import models
from books.models import Book
from users.models import MyUser
#from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Comment(models.Model):
    text = models.TextField(null=False)
    rating = models.FloatField(null=False)
    #user = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="comments", null=False)
    
    class Meta:
        constraints =  [
            models.CheckConstraint(
                check=models.Q(rating__gte=1) & models.Q(rating__lt=5),
                name="Rating value is valid between 1 and 5",
            )
        ]