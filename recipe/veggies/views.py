from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Recipe

# Create your views here.


def accept_response(req):
    if req.method=='POST':
        data = req.POST

        recipe_name = data.get('name')
        recipe_description = data.get('description')
        recipe_image= req.FILES.get('image')

        print(recipe_name)
        print(recipe_description)
        print(recipe_image)

 # storing in db 
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_image = recipe_image
        )
        return redirect('/recipe/') # why to do redirect 
    
    queryset = Recipe.objects.all()

    
    return render(req,'recipeform.html',{'recipes':queryset})


def delete_recipe(req,id):

    query = Recipe.objects.get(id=id)
    query.delete()
    return redirect('/recipe/')
    print(id)
    # return HttpResponse('a')