from django.urls import path
from .views import CreateUserView, LoginView

urlpatterns = [
    
    path('api/register/', CreateUserView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    
]