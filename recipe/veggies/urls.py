
from django.urls import path

from . import views 

urlpatterns = [
    path('recipe/',views.accept_response)    
]
