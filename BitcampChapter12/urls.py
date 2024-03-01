from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('event-planner/', include('EventPlanner.urls')),
    path('note-taking/', include('NoteTaking.urls')),
    path('recipe-manager/', include('RecipeManager.urls')),
]
