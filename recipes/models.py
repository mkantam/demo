from django.db import models
RECIPE_CATEGORIES = [('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner'),('Salad','Salad'),('Baked-goods','Baked-goods')]

# Create your models here.
class Recipe(models.Model):
    recipe_id = models.BigAutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    serving_size = models.IntegerField()
    category = models.CharField(choices=RECIPE_CATEGORIES, default='Breakfast', max_length=100)
    notes = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['recipe_id']