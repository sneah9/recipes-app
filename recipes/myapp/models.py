from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    #picture = models.ImageField(upload_to='recipe', default=)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    unit = models.CharField(max_length=200)


class Relationship(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)