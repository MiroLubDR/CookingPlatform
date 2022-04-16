from django.urls import path
from djangoProject1.web.views import HomeView
from  djangoProject1.web.views import Top10ListView, RecipeCreateView,RecipeListView,RecipeEditView,RecipeDetails,RecipeDeleteView,RecipeUserListView
urlpatterns = [
    path('createRecipe/',RecipeCreateView.as_view(),name = 'Recipe create'),

    path('Recipeslist/', RecipeListView.as_view(), name='Recipe list'),
    path('Top10/', Top10ListView.as_view(), name='Top 10'),
    path('MyRecipeslist/', RecipeUserListView.as_view(), name='My Recipe list'),
    path('recipedetail/<slug:pk>', RecipeDetails.as_view(), name='Recipe details'),
    path('editRecipe/<slug:pk>',RecipeEditView.as_view(),name = 'Recipe edit'),
    path('recipedelete/<slug:pk>' ,RecipeDeleteView.as_view(),name= 'Recipe Delete')



]