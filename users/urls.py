from django.urls import path
from .views import RegisterView, LoginView, LogoutView, RegisterPageView, LoginPageView, LandingPageView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_page/', RegisterPageView.as_view(), name='register_page'),
    path('', LoginPageView.as_view(), name='login_page'),
    path('landing_page/', LandingPageView.as_view(), name='landing_page'),
]
