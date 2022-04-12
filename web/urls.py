from django.urls import path
from djangoProject1.web.views import HomeView
from  djangoProject1.web.views import RecipeCreateView
urlpatterns = [
    path('createRecipe/',RecipeCreateView.as_view(),name = 'Recipe create')


]