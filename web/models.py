
from django.contrib.postgres.fields import ArrayField
from django.db import models

from djangoProject1.accounts.models import YouCookUser


class Recipe_likes(models.Model):
    pass

class Recipe(models.Model):

    recipe_img = models.ImageField(
        null= True,
        blank= True,





    )

    recipe_name = models.CharField(
        max_length= 30
    )

    products = ArrayField(
        ArrayField(
            models.CharField(max_length=20, blank=True),
            size=30,
        ),
        size=30,
    )

    description = models.CharField(
        max_length= 1000,
        verbose_name= 5,
    )
    recipe_views_count = models.IntegerField(
        default= 0,

    )
    recipe_likes = models.ImageField(
        default=0,
    )
    post_date = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.OneToOneField(
        YouCookUser,
        on_delete= models.CASCADE,
        related_name = 'recipes'
    )

class Recipe_comments(models.Model):
    author = models.CharField(
        max_length= 30

    )

    content = models.CharField(
        max_length= 999
    )

    user = models.OneToOneField(
        YouCookUser,
        on_delete= models.CASCADE
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )