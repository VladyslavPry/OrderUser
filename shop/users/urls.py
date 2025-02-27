from django.urls import path
from .views import RegisterView, LogoutView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]
