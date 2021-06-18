from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    contexto = "<h1>ESTE ES EL INDICE</h1>"
    titulo = 'Inicio'
    return render(request, 'layout/layout.html', {'context':contexto, 'title': titulo})

#crear Empresas
class EmpresasCreateView(CreateView):
    model= Empresas
    form_class=  EmpresaForm#aqui va el formulario
    template_name= 'formularios/create-companies.html'#aqui donde se va crear el registr
    success_url= reverse_lazy('empresas')#donde se va redigir el contenido

#listar las empresas
class EmpresasListView(ListView):
    model= Empresas
    template_name= 'listado/empresas.html'

#actualizar Empresas
class EmpresaUpdateView(UpdateView):
    model= Empresas
    form_class=  EmpresaForm#aqui va el formulario
    template_name= 'formularios/create-companies.html'#aqui donde se va crear el registr
    success_url= reverse_lazy('empresas')#donde se va redigir el contenido


#crear clientes
class CustomerCreateView(CreateView):
    model= Customers
    form_class = CustomerForm
    template_name= 'formularios/create-customer.html'
    success_url = reverse_lazy('customers')

#listar clientes
class CustomerListView(ListView):
    model= Customers
    template_name = 'listado/customer.html'


#crear Servicios
class ServicesCreateView(CreateView):
    model= Services
    form_class= ServicesForm
    template_name = 'formularios/create-service.html'
    success_url = reverse_lazy('services')

#listar servicios
class ServicesListView(ListView):
    model=Services
    template_name= 'listado/services.html'

#Crear solicitudes
class SolicitudCreateView(CreateView):
    model=Solicitudes
    form_class= SolicitudForm
    template_name= 'formularios/create-request.html'
    success_url = reverse_lazy('solicitud')

#listar solicitudes
class SolicitudListView(ListView):
    model = Solicitudes
    template_name = 'listado/solicitudes.html'

#crear Levantamientos de campo
class SurveyCreateView(CreateView):
    model = FieldSurvey
    form_class = SurveyForm
    template_name = 'formularios/create-survey.html'
    success_url = reverse_lazy('levantamientos')


#listar Levantamiento de Campo
class SurveyListView(ListView):
    model = FieldSurvey
    template_name = 'listado/surveys.html'


#Crear Informes
class ReportCreateView(CreateView):
    model = Reports
    form_class = ReportForm
    template_name = 'formularios/create-report.html'
    success_url = reverse_lazy('reports')

#Listar Informes

class ReportListView(ListView):
    model = Reports
    template_name = 'listado/reports.html'


#crear Curvas De Nivel
class LevelCreateView(CreateView):
    model = levelCurves
    form_class = LevelForm
    template_name = 'formularios/create-level.html'
    success_url = reverse_lazy('levels')

#Listar Curvas de Nivel
class LevelListView(ListView):
    model = levelCurves
    template_name = 'listado/levels.html'


#crear Catastros
class CadastralCreateView(CreateView):
    model = CadastralPlans
    form_class = CadastralForm
    template_name = 'formularios/create-cadastral.html'
    success_url = reverse_lazy('cadastral')

#listar Catastros
class CadastralListView(ListView):
    model = CadastralPlans
    template_name = 'listado/cadastral.html'

#crear Correciones

#listar correciones

#crear replanteo
class ReplantCreateView(CreateView):
    model = Replant
    form_class = ReplantForm
    template_name = 'formularios/create-replant.html'
    success_url = reverse_lazy('replant')

#listar replanteos
class ReplantListView(ListView):
    model = Replant
    template_name = 'listado/replant.html'


