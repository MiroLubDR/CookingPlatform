from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.views.generic import CreateView

from djangoProject1.web.forms import RecipeForm



class HomeView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context




def show_register(request):
    return render(request, 'register_template.html')

class RecipeCreateView(CreateView):
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