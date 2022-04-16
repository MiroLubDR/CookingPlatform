from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from djangoProject1.accounts.models import YouCookUser
from djangoProject1.web.forms import RecipeForm
from djangoProject1.web.models import Recipe

def top_10_selection(array):
    return array[:2]


class HomeView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

class RecipeCreateView(LoginRequiredMixin,views.CreateView):
    login_url = reverse_lazy('Register')

    form_class = RecipeForm
    template_name = 'web/recipeCreatePage.html'
    success_url = reverse_lazy('Home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class RecipeDetails(LoginRequiredMixin,views.DetailView):
    login_url = reverse_lazy('Login')

    model = Recipe
    template_name = 'web/recipeDetailPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return  context



class RecipeListView(views.ListView):


    model = Recipe
    paginate_by = 5
    queryset = model.objects.order_by('-post_date')
    context_object_name = 'recipe_list'
    template_name = 'web/RecipesListTemplate.html'

class Top10ListView(views.ListView):


    model = Recipe
    paginate_by = 5
    queryset = top_10_selection(model.objects.order_by('-post_date'))
    context_object_name = 'recipe_list'
    template_name = 'web/RecipesListTemplate.html'


class RecipeUserListView(LoginRequiredMixin,views.ListView):
    login_url = reverse_lazy('Register')

    model = Recipe
    queryset = model.objects.order_by('-post_date')
    context_object_name = 'my_recipes'
    template_name = 'web/RecipesMyRecipesTemplate.html'


    def get_queryset(self):
        """
        Return the list of items for this view.

        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        if self.queryset is not None:
            queryset = self.queryset
            if isinstance(queryset, QuerySet):
                queryset = queryset.all().filter(user = self.request.user.id)
        elif self.model is not None:
            queryset = self.model._default_manager.all()
        else:
            raise ImproperlyConfigured(
                "%(cls)s is missing a QuerySet. Define "
                "%(cls)s.model, %(cls)s.queryset, or override "
                "%(cls)s.get_queryset()." % {"cls": self.__class__.__name__}
            )
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        print(queryset)
        return queryset








class RecipeEditView(LoginRequiredMixin,views.UpdateView):
    login_url = reverse_lazy('Register')

    model = Recipe
    template_name = 'web/recipeEditPage.html'
    fields = ['recipe_img','recipe_name','products','description']
    success_url = reverse_lazy('Recipe list')

    def put(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return  self.post(kwargs)



class RecipeDeleteView(LoginRequiredMixin,views.DeleteView):
    login_url = reverse_lazy('Register')

    model = Recipe
    success_url = reverse_lazy('Recipe list')
    template_name = 'web/recipeDeletePage.html'


