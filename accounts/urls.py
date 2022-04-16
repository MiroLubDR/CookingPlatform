from django.urls import path

from djangoProject1.accounts.views import UserLoginView, UserRegisterView, UserLogOutView, ProfileView, \
    ProfileSetInformationView, ProfileEditView, ChangePassword

urlpatterns = [
    path('Login/', UserLoginView.as_view(), name='Login'),
    path('register/', UserRegisterView.as_view(), name='Register'),
    path('passwordreset/<slug:pk>', ChangePassword.as_view(), name='Change Password'),
    path('logout/', UserLogOutView.as_view(), name='LogOut'),

    path('profile/',ProfileView.as_view(), name = 'Profile'),
    path('profile/setprofile/', ProfileSetInformationView.as_view(),name='ProfileSetInfo'),
    path('profile/editprofile/<slug:pk>/',ProfileEditView.as_view(),name = 'ProfileEdit')
]