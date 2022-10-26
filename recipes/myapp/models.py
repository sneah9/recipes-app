from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
