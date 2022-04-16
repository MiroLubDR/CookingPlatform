from django.db import models
from django.contrib.auth import models as auth_models, get_user_model

from djangoProject1.Validators.Validators import rude_words_validator
from djangoProject1.accounts.managers import YouCookUserManager

# CookUser = get_user_model()


class YouCookUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 27
    USER_EMAIL_MAX_LENGTH = 200

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    userEmail = models.EmailField(
        max_length=USER_EMAIL_MAX_LENGTH,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = YouCookUserManager()

class YouCookUserProfile(models.Model):

    FIRST_NAME_MAX_LENGTH  = 14
    LAST_NAME_MAX_LENGTH  = 15

    first_name = models.CharField(
        max_length= FIRST_NAME_MAX_LENGTH,
        blank = False,
        null = False

    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        blank=False,
        null=False

    )

    profile_image = models.ImageField(
        blank = True,
        null = True,
    )

    profile_description = models.CharField(
        max_length= 800,
        validators= [rude_words_validator,]


    )
    user = models.OneToOneField(
        YouCookUser,
        on_delete= models.CASCADE,
        primary_key= True,
        related_name= 'profile'
    )

    def get_full_name (self,):
        firstName = self.first_name
        lastName = self.last_name

        return f'{firstName} {lastName}'
