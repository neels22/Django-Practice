
from django.urls import path

from . import views 

urlpatterns = [
    path('recipe/',views.accept_response),
    path('delete-recipe/<id>',views.delete_recipe) ,
    path('update-recipe/<id>',views.update_recipe) ,
]
