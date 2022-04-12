
from django.contrib.auth import forms, get_user_model
from django import forms as djangoForms

from djangoProject1.accounts.models import  YouCookUserProfile

user_model = get_user_model()

class UserRegisterForm(forms.UserCreationForm):



    def __init__(self,*args,**kwargs):
        super(UserRegisterForm, self).__init__(*args,**kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = user_model
        help_texts = None
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': djangoForms.TextInput(
                attrs={
                    'class':'accaount__form input_fields',
                    'placeholder':'Enter your username'

                }
            ),
        }

    password1 = djangoForms.CharField(widget=djangoForms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'accaount__form input_fields',
                                                                  }),
                                                                    label= 'Password')
    password2 = djangoForms.CharField(widget=djangoForms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'accaount__form input_fields',

                                                                  }),
                                                                    label= 'Re-Password')


class ProfileInformationForm(djangoForms.ModelForm):
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
        model = YouCookUserProfile
        fields = ['first_name','last_name','profile_destcription','profile_image',]
    pass
