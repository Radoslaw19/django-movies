from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} from {self.released}"

# class Genre(models.Model):
#     name = models.CharField(max_length=20, unique=True)
#
#     def __str__(self):
#         return self.name