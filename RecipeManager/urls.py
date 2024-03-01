from django.urls import path
from .views import *

urlpatterns = [
    path('', recipe_index, name='recipe_index'),
    path('add/', recipe_add, name='recipe_add'),
    path('<int:id>/', recipe_details, name='recipe_details'),
]