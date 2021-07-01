from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
import datetime


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Empresa'
        context['buttom'] = 'Crear Registro'
        return context
    


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Cliente'
        context['buttom'] = 'Actualizar Registro'
        return context


#crear clientes
class CustomerCreateView(CreateView):
    model= Customers
    form_class = CustomerForm
    template_name= 'formularios/create-customer.html'
    success_url = reverse_lazy('customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Cliente'
        context['buttom'] = 'Crear Registro'
        return context

#listar clientes
class CustomerListView(ListView):
    model= Customers
    template_name = 'listado/customer.html'

#actualizar Clientes
class CustomerUpdateView(UpdateView):
    model= Customers
    form_class = CustomerForm
    template_name= 'formularios/create-customer.html'
    success_url = reverse_lazy('customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Cliente'
        context['buttom'] = 'Actualizar Registro'
        return context


#crear Servicios
class ServicesCreateView(CreateView):
    model= Services
    form_class= ServicesForm
    template_name = 'formularios/create-service.html'
    success_url = reverse_lazy('services')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Servicio'
        context['buttom'] = 'Crear Registro'
        return context

#listar servicios
class ServicesListView(ListView):
    model=Services
    template_name= 'listado/services.html'


#actualizar Servicios
class ServicesUpdateView(UpdateView):
    model= Services
    form_class= ServicesForm
    template_name= 'formularios/create-service.html'
    success_url = reverse_lazy('services')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Servicio'
        context['buttom'] = 'Actualizar Registro'
        return context

#Crear solicitudes
class SolicitudCreateView(CreateView):
    model=Solicitudes
    form_class= SolicitudForm
    template_name= 'formularios/create-request.html'
    success_url = reverse_lazy('solicitud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Solicitud'
        context['buttom'] = 'Crear Registro'
        context['date'] = datetime.date
        return context

#listar solicitudes
class SolicitudListView(ListView):
    model = Solicitudes
    template_name = 'listado/solicitudes.html'

#actualizar Solicitud
class SolicitudUpdateView(UpdateView):
    model= Solicitudes
    form_class= SolicitudForm
    template_name= 'formularios/create-request'
    success_url = 'solicitud'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Solicitud'
        context["title"] = 'Actualizar Registro'
        return context
    

#crear Levantamientos de campo
class SurveyCreateView(CreateView):
    model = FieldSurvey
    form_class = SurveyForm
    template_name = 'formularios/create-survey.html'
    success_url = reverse_lazy('levantamientos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Levantamiento'
        context['buttom'] = 'Crear Registro'
        return context


#listar Levantamiento de Campo
class SurveyListView(ListView):
    model = FieldSurvey
    template_name = 'listado/surveys.html'

#actualizar levantamiento
class SurveyUpdateView(UpdateView):
    model = FieldSurvey
    form_class = SurveyForm
    template_name = 'formularios/create-survey.html'
    success_url = reverse_lazy('levantamientos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Levantamiento'
        context['buttom'] = 'Actualizar Registro'
        return context

#Crear Informes
class ReportCreateView(CreateView):
    model = Reports
    form_class = ReportForm
    template_name = 'formularios/create-report.html'
    success_url = reverse_lazy('reports')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Informe'
        context['buttom'] = 'Crear Registro'
        return context

#Listar Informes

class ReportListView(ListView):
    model = Reports
    template_name = 'listado/reports.html'

#Actualizar Informes
class ReportUpadateView(UpdateView):
    model = Reports
    form_class = ReportForm
    template_name = 'formularios/create-report.html'
    success_url = reverse_lazy('reports')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Informe'
        context['buttom'] = 'Actualizar Registro'
        return context


#crear Curvas De Nivel
class LevelCreateView(CreateView):
    model = levelCurves
    form_class = LevelForm
    template_name = 'formularios/create-level.html'
    success_url = reverse_lazy('levels')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Curvas'
        context['buttom'] = 'Crear Registro'
        return context

#Listar Curvas de Nivel
class LevelListView(ListView):
    model = levelCurves
    template_name = 'listado/levels.html'

#Actualizar Curvas
class LevelUpdateView(UpdateView):
    model = levelCurves
    form_class = LevelForm
    template_name = 'formularios/create-level.html'
    success_url = reverse_lazy('levels')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Curvas'
        context['buttom'] = 'Actualizar Registro'
        return context


#crear Catastros
class CadastralCreateView(CreateView):
    model = CadastralPlans
    form_class = CadastralForm
    template_name = 'formularios/create-cadastral.html'
    success_url = reverse_lazy('cadastral')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Catastro'
        context['buttom'] = 'Crear Registro'
        return context

#listar Catastros
class CadastralListView(ListView):
    model = CadastralPlans
    template_name = 'listado/cadastral.html'

#Actualizar Catastros
class CadastralUpdateView(UpdateView):
    model = CadastralPlans
    form_class = CadastralForm
    template_name = 'formularios/create-cadastral.html'
    success_url = reverse_lazy('cadastral')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Catastro'
        context['buttom'] = 'Actualizar Registro'
        return context

#crear Correciones

#listar correciones

#crear replanteo
class ReplantCreateView(CreateView):
    model = Replant
    form_class = ReplantForm
    template_name = 'formularios/create-replant.html'
    success_url = reverse_lazy('replant')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Replanteo'
        context['buttom'] = 'Crear Registro'
        return context

#listar replanteos
class ReplantListView(ListView):
    model = Replant
    template_name = 'listado/replant.html'

#Actualizar Replanteo
class ReplantUpdateView(UpdateView):
    model = Replant
    form_class = ReplantForm
    template_name = 'formularios/create-replant.html'
    success_url = reverse_lazy('replant')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Replanteo'
        context['buttom'] = 'Actualizar Registro'
        return context    


