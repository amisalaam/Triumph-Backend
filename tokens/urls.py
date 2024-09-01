from django.urls import path
from .views import *

urlpatterns = [
    path('tickets/', TicketManagementView.as_view(), name='register'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    
    path('customer/support/', CustomerSupportTeamListView.as_view(), name='register'),
    
]