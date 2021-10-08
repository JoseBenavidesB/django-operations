from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Department)
admin.site.register(Ocupations)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone_number', 'ocupation', 'department')
admin.site.register(Employees, EmployeesAdmin)

class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefix')
admin.site.register(Empresas, EmpresasAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastName', 'nacionalidad', 'email', 'phoneNumber')
admin.site.register(Customers, CustomerAdmin)

class QuotesAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'customer', 'amount','status','date')
admin.site.register(Quotes, QuotesAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('quote', 'bill1', 'amount_bill1', 'date_bill1','bill2', 'amount_bill2', 'date_bill2')
admin.site.register(Payments, PaymentsAdmin)

""" class PreliminaryAdmin(admin.ModelAdmin):
    list_display = ('quote', 'assigned_to', 'locationMark', 'googleMaps', 'sketch', 'document', 'status')
admin.site.register(Preliminary, PreliminaryAdmin)

admin.site.register(Services) """

""" class SolicitudesAdmin(admin.ModelAdmin):
    list_display = ('quote','deliveryDate','status')
admin.site.register(Solicitudes, SolicitudesAdmin) """

""" class FieldSurveyAdmin(admin.ModelAdmin):
    list_display = ('solicitud_id', 'assigned_to', 'proposedDate', 'fieldSurveyDate', 'conclusionDate', 'downloadedData')
admin.site.register(FieldSurvey, FieldSurveyAdmin) """

#admin.site.register(Draw)
#admin.site.register(Reports)
#admin.site.register(levelCurves)
#admin.site.register(CadastralPlans)
#admin.site.register(Replant)
    