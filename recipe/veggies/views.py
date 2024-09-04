from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User

from .models import Recipe
from django.contrib import messages
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

    if req.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = req.GET.get('search'))
    
    return render(req,'recipeform.html',{'recipes':queryset})


def delete_recipe(req,id):

    query = Recipe.objects.get(id=id)
    query.delete()
    return redirect('/recipe/')

    # return HttpResponse('a')


def update_recipe(req,id):
    queryset = Recipe.objects.get(id=id)

    if req.method == "POST":
        data = req.POST
        recipe_name = data.get('name')
        recipe_description = data.get('description')
        recipe_image= req.FILES.get('image')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/recipe/')



    return render(req,'update_form.html',{'recipes':queryset})



def login(req):

    return render(req,'login.html',{})


def register(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        # Check if email or password is missing
        if not email or not password:
            messages.error(req, "Both email and password are required!")
            return redirect('/register/')

        # Check if user with this email already exists
        if User.objects.filter(email=email).exists():
            messages.error(req, "User with this email already exists!")
            return redirect('/register/')

        # Create the user
        user = User.objects.create(
            username=email,  # Setting username as email
            email=email,
        )
        user.set_password(password)  # Hashing the password
        user.save()

        messages.success(req, "Registration successful! You can now log in.")
        return redirect('/login/')  # Redirect to login page after successful registration

    return render(req, 'register.html', {})