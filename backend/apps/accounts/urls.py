
from django.urls import path

from .views import CustomerRegistrationView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path(
        'register/',
        CustomerRegistrationView.as_view(),
        name='customer-register'
    ),

    path(
        'login/',
        LoginView.as_view(),
        name='user-login'
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token-refresh'
    ),
]
