
from django.urls import path

from .views import CustomerRegistrationView, LoginView,LogoutView
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

    path(
        'logout/',
        LogoutView.as_view(),
        name='user-logout'
    ),
]
