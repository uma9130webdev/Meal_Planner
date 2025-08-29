from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_planner, name='meal_planner'),
    path('home/',views.home,name="home"),path('delete/day/<int:pk>/', views.delete_day, name='delete_day'),
    path('delete/meal/<int:pk>/', views.delete_meal, name='delete_meal'),
    path('delete/recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('delete/grocery/<int:pk>/', views.delete_grocery_item, name='delete_grocery'),
]
