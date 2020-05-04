from django.shortcuts import render
from recipe_box.models import Author, RecipeItems

def index(request):
    items = RecipeItems.objects.all()
    return (request, "index.html", {"data": "items"})

def recipes(request):
    ingredient = stuff.objects.all()
    return render(request, "recipe.html", {"list": "ingredient"})