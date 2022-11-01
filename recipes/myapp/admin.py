from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Relationship

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Relationship)



