from django.contrib import admin
from .models import Ticket, CustomerSupportTeam

# Register your models here.

admin.site.register(Ticket)
admin.site.register(CustomerSupportTeam)