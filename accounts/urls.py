from django.urls import path

from djangoProject1.accounts.views import UserLoginView, UserRegisterView, UserLogOutView, ProfileView, \
    ProfileSetInformationView, ProfileEditView

urlpatterns = [
    path('Login/', UserLoginView.as_view(), name='Login'),
    path('register/', UserRegisterView.as_view(), name='Register'),
    path('logout/', UserLogOutView.as_view(), name='LogOut'),

    path('profile/',ProfileView.as_view(), name = 'Profile'),
    path('profile/setprofile/', ProfileSetInformationView.as_view(),name='ProfileSetInfo'),
    path('profile/editprofile/',ProfileEditView.as_view(),name = 'ProfileEdit')
]