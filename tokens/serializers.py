# serializers.py
from rest_framework import serializers
from .models import Ticket, CustomerSupportTeam

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'priority', 'status', 'user', 'assigned_to']
        extra_kwargs = {
            'user': {'read_only': True},
        }

class CustomerSupportTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSupportTeam
        fields = ['id', 'name']