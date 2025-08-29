from django.shortcuts import render, redirect,get_object_or_404
from .models import Day, Meal, Recipe, GroceryItem
from .forms import MealForm, RecipeForm, GroceryForm

def meal_planner(request):
    days = Day.objects.all()
    meals = Meal.objects.all()
    recipes = Recipe.objects.all()
    grocery_list = GroceryItem.objects.all()

    meal_form = MealForm()
    recipe_form = RecipeForm()
    grocery_form = GroceryForm()

    if request.method == 'POST':
        if 'add_meal' in request.POST:
            meal_form = MealForm(request.POST)
            if meal_form.is_valid():
                meal_form.save()
                return redirect('meal_planner')
        elif 'add_recipe' in request.POST:
            recipe_form = RecipeForm(request.POST, request.FILES)
            if recipe_form.is_valid():
                recipe_form.save()
                return redirect('meal_planner')
        elif 'add_grocery' in request.POST:
            grocery_form = GroceryForm(request.POST)
            if grocery_form.is_valid():
                grocery_form.save()
                return redirect('meal_planner')

    context = {
        'days': days,
        'meals': meals,
        'recipes': recipes,
        'grocery_list': grocery_list,
        'meal_form': meal_form,
        'recipe_form': recipe_form,
        'grocery_form': grocery_form,
    }
    return render(request, 'enroll/meal_planner.html', context)
def home(request):
    days = Day.objects.all()
    meals = Meal.objects.all()
    recipes = Recipe.objects.all()
    grocery_list = GroceryItem.objects.all()

    context = {
        'days': days,
        'meals': meals,
        'recipes': recipes,
        'grocery_list': grocery_list,
    }
    return render(request, 'enroll/home.html', context)


def delete_day(request, pk):
    day = get_object_or_404(Day, pk=pk)
    day.delete()
    return redirect('home')

def delete_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    meal.delete()
    return redirect('home')

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('home')

def delete_grocery_item(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return redirect('home')