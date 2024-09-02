# serializers.py
from rest_framework import serializers
from .models import Ticket, CustomerSupportTeam

#Serializer for ticket
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'priority', 'status', 'user', 'assigned_to']
        extra_kwargs = {
            'user': {'read_only': True},
        }
        
#Serializer for Customer Support Team
class CustomerSupportTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSupportTeam
        fields = ['id', 'name']