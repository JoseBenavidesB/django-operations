from django.db.models import fields
from django.forms import ModelForm
from .models import *

class EmpresaForm(ModelForm):
    class Meta:
        model = Empresas
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customers
        fields = '__all__'

class ServicesForm(ModelForm):
    class Meta:
        model=Services
        fields = '__all__'

class SolicitudForm(ModelForm):
    class Meta:
        model = Solicitudes
        fields = 'quote', 'customer_id', 'service_id', 'contact', 'deliveryDate', 'plan', 'status'

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

class CorrectionForm(ModelForm):
    class Meta:
        model = Corrections
        fields = '__all__'