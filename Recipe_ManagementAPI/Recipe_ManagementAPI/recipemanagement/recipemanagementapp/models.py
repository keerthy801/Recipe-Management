from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=100)
    ingredients = models.TextField()
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Review_or_Comment(models.Model):
    recipe_id=models.ForeignKey(Recipe,related_name='reviews',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(null=True,blank=True)
    review=models.TextField()
    comment=models.CharField(max_length=600,null=True,blank=True)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe_id.name






