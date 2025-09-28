from django.urls import path,include
from account.views import UserRegistrationView
from account.views import UserloginView
from account.views import UserProfileView
from account.views import UserChangePasswordView
from account.views import sendPasswordResetEmailView
from account.views import UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserloginView.as_view(),name='login'),
    path('profile/', UserProfileView.as_view(),name='Profile'),
    path('changepassword/', UserChangePasswordView.as_view(),name='ChangePasswordView'),
    path('send-reset-password-email/', sendPasswordResetEmailView.as_view(),name='Send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(),name='reset-password'),
    
]





