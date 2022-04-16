from django import forms as djangoForms

from djangoProject1.web.models import Recipe


class RecipeForm(djangoForms.ModelForm):
    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.user = user
    def save(self, commit=True):
        u =super().save(commit=False)
        u.user = self.user
        if commit :
            u.save()
        return u
        pass

    class Meta:
        model = Recipe
        fields = ['recipe_img','recipe_name','products','description']
        widgets ={
            'description':djangoForms.Textarea(
                attrs={'rows':5,'cols':60,'class': 'form_control','title': 'description' },

            )}