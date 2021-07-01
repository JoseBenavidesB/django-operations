from django.contrib import admin
from .models import *
# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    

    admin.site.register(Empresas)
    admin.site.register(Customers)
    admin.site.register(Services)
    admin.site.register(Solicitudes)
    admin.site.register(FieldSurvey)
    admin.site.register(Reports)
    admin.site.register(levelCurves)
    admin.site.register(CadastralPlans)
    admin.site.register(Replant)
    