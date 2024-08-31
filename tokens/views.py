from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer



class TicketManagementView(APIView):
    permission_classes = [IsAuthenticated]
    
    # Create a new ticket (only superuser)
    def post(self, request):
        if not request.user.is_superuser:
            return Response({"detail": "Unauthorized: You do not have permission to perform this action."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #List all tickets with optional filters
    def get(self, request):
        tickets = Ticket.objects.all()

        # Apply filters
        status_filter = request.query_params.get('status')
        priority_filter = request.query_params.get('priority')
        user_filter = request.query_params.get('user')

        if status_filter:
            tickets = tickets.filter(status=status_filter)
        if priority_filter:
            tickets = tickets.filter(priority=priority_filter)
        if user_filter:
            tickets = tickets.filter(user_id=user_filter)

        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)
    


class TicketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    #Retrieve a specific ticket
    def get(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk, user=request.user)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data)
        except Ticket.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
    def put(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk, user=request.user)
            serializer = TicketSerializer(ticket, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        # Check if the user is a superuser
        if not request.user.is_superuser:
            return Response({"detail": "You do not have permission to delete this ticket."}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            ticket = Ticket.objects.get(pk=pk, user=request.user)
            ticket.delete()
            return Response({"detail": "Ticket deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
        

    

