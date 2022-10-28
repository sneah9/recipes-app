from django.shortcuts import render

from django.http import HttpResponse

from .models import * #(Recipe, Ingredient)

def index(request):
    return HttpResponse("Hello, world!")

def recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe_details.html', {'recipe':recipe})