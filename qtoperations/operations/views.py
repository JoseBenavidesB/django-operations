from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
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


    # #to send the errros at template
    # def post(self, request, *args, **kwargs) :
    #     #return super().post(request, *args, **kwargs)
    #     form = ServicesForm(request.POST)
    #     if form.is_valid():
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Empresa'
        context['buttom'] = 'Crear Registro'
        return context
    
    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#listar las empresas

class EmpresasListView(ListView):
    model= Empresas
    template_name= 'listado/empresas.html'

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
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

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#listar clientes
class CustomerListView(ListView):
    model= Customers
    template_name = 'listado/customer.html'

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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
    
    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#listar servicios
class ServicesListView(ListView):
    model=Services
    template_name= 'listado/services.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
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
        context['date'] = datetime.date.today()
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#listar solicitudes
class SolicitudListView(ListView):
    model = Solicitudes
    template_name = 'listado/solicitudes.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#actualizar Solicitud
class SolicitudUpdateView(UpdateView):
    model= Solicitudes
    form_class= SolicitudForm
    template_name= 'formularios/create-request.html'
    success_url = reverse_lazy('solicitud')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Solicitud'
        context["buttom"] = 'Actualizar Registro'
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#Detalles
class ReportDetailView(DetailView):
    model= Solicitudes
    template_name='detalles/detail.html'

    

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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#listar Levantamiento de Campo
class SurveyListView(ListView):
    model = FieldSurvey
    template_name = 'listado/surveys.html'


    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Listar Informes

class ReportListView(ListView):
    model = Reports
    template_name = 'listado/reports.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)






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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#Listar Curvas de Nivel
class LevelListView(ListView):
    model = levelCurves
    template_name = 'listado/levels.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#listar Catastros
class CadastralListView(ListView):
    model = CadastralPlans
    template_name = 'listado/cadastral.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


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

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
  


class LoginFormView(LoginView):
    template_name= 'formularios/login.html'


    "make a comprobation to know if user is authenticated or not"
    def dispatch(self, request, *args,**kwargs): 
        if request.user.is_authenticated:
            return redirect('solicitud')

        return super().dispatch(request, *args, **kwargs)
    """LOGIN_REDIRECT_URL is neccesary to redirect after login, this variable in settings"""


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Inicio de Sesión'
        context['buttom'] = 'Iniciar Sesión'
        return context   


class LogoutFormView(LogoutView):
    next_page= 'inicio'


# LISTAR Todo lo de una solicitud
def complete_request(request, servicio, id):
    campo = Solicitudes.objects.get(id=id).fieldsurvey_set.all()
    solicitud = Solicitudes.objects.get(id=id)
    template=''
    service=''
    if servicio == 'Informe':
        service = Solicitudes.objects.get(id=id).solicitudReport.all() 
        template='detalles/detail-report.html'
    elif servicio == 'Plano Catastrado':
        service = Solicitudes.objects.get(id=id).solicitudCadastral.all() 
        template='detalles/detail-catastro.html'
    elif servicio == 'Replanteo':
        service = Solicitudes.objects.get(id=id).solicitudReplant.all() 
        template='detalles/detail-replant.html'
    else:
        service = Solicitudes.objects.get(id=id).solicitudLevel.all() 
        template='detalles/detail-level.html'  
        
    return render(request, template, {'solicitud':solicitud, 'service':service, 'campo': campo})

#puedo usar una vista donde se agrega al context de los modelos Informes, Catastro, Reporte, Replanteo, Lev Campo y Solicitudes
#se debe filtrar id.informe = id.