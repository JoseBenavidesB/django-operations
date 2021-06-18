from django.contrib import admin
from .models import *
# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    

    admin.site.register(Empresas)
    admin.site.register(Customers)
