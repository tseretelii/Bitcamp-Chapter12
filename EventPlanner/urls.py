from django.urls import path
from .views import *

urlpatterns = [
    path('', event_index, name='event_index'),
    path('add/', event_add, name = 'event_add'),
    path('edit/<str:title>', event_edit, name = 'event_edit'),
    path('delete/<str:title>', event_delete, name= 'event_delete')
]