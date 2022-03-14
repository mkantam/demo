from django.contrib import admin

# Register your models here.
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_name', 'ingredients', 'instructions', 'serving_size', 'category']

admin.site.register(Recipe, RecipeAdmin)
