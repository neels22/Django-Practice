
from django.urls import path

from . import views 

urlpatterns = [
    path('recipe/',views.accept_response),
    path('delete-recipe/<id>',views.delete_recipe) ,
    path('update-recipe/<id>',views.update_recipe) ,
    path('login/',views.login_page) ,
    path('register/',views.register) ,
    path('logout/',views.logout_page) ,
]
