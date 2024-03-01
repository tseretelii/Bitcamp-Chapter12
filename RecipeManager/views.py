from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def recipe_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_index.html', {'recipes':recipes})

def recipe_add(request):
    if request.method == 'POST':
        new_recipe = Recipe(
            name = request.POST.get('name'),
            ingredients = request.POST.get('ingredients'),
            instructions = request.POST.get('instructions')
        )
        new_recipe.save()
        return redirect('recipe_index')
    return render(request, 'recipe_add.html')

def recipe_details(request, id):
    recipe = Recipe.objects.get(id = id)
    return render(request, 'recipe_details.html', {'recipe': recipe})