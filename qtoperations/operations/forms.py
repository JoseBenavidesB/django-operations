from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import *
from django.db import models

class SubCustomerForm(ModelForm):
    class Meta:
        model = Sub_customers
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customers
        fields = '__all__'

class QuoteForm(ModelForm):
    class Meta:
        model = Quotes
        fields = '__all__'
class PayForm(ModelForm):
    class Meta:
        model = Payments
        fields = '__all__'
class PreliminaryForm(ModelForm):
    class Meta:
        model = Preliminary
        fields = '__all__'

class ServicesForm(ModelForm):
    class Meta:
        model=Services
        fields = '__all__'

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitudes
        fields = 'quote', 'deliveryDate', 'plan', 'status'

class SurveyForm(ModelForm):
    class Meta:
        model = FieldSurvey
        fields = '__all__'

class ReportForm(ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
    
class LevelForm(ModelForm):
    class Meta:
        model = levelCurves
        fields = '__all__'

class CadastralForm(ModelForm):
    class Meta:
        model = CadastralPlans
        fields = '__all__'

class ReplantForm(ModelForm):
    class Meta:
        model = Replant
        fields = '__all__'

class CorregirAPT(ModelForm):
    class Meta:
        model = Corrections
        fields = '__all__'