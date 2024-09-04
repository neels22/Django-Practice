from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField(max_length=300)
    recipe_image = models.ImageField()

    def __str__(self) -> str:
        return f"{self.recipe_name}"