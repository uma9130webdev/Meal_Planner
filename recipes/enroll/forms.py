from django import forms
from .models import Meal, Recipe, GroceryItem

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['day', 'meal_type', 'description']
        

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']

class GroceryForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name']
from django import forms



