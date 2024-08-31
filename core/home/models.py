from django.db import models

# Create your models here.




class Student(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(null=True,blank=True)
    file = models.FileField(null=True,blank=True)


