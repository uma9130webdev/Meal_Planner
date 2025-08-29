from django.db import models

class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Meal(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day.name} - {self.meal_type}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.title

class GroceryItem(models.Model):
    name = models.TextField(max_length=500)

    def __str__(self):
        return self.name
