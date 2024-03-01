from django.urls import path
from .views import *

urlpatterns = [
    path('', note_index, name='note_index'),
    path('add/', note_add, name='note_add'),
    path('edit/<str:title>', note_edit, name='note_edit'),
    path('delete/<int:id>', note_delete, name='note_delete')
]