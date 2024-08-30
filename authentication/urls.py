from django.urls import path
from .views import CreateUserView

urlpatterns = [
    
    path('api/register/', CreateUserView.as_view(), name='register'),
    
]