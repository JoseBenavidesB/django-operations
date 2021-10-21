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
    contexto = "Bienvenido, por favor selecciona una opción de la barra superior"
    titulo = 'Inicio'
    return render(request, 'layout/layout.html', {'context':contexto, 'title': titulo})

#crear Empresas

class EmpresasCreateView(CreateView):
    model= Sub_customers
    form_class=  SubCustomerForm#aqui va el formulario
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
    model= Sub_customers
    template_name= 'listado/empresas.html'

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#actualizar Empresas
class EmpresaUpdateView(UpdateView):
    model= Sub_customers
    form_class=  SubCustomerForm#aqui va el formulario
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


#Crear Cotizaciones
class QuoteCreateView(CreateView):
    model = Quotes
    form_class = QuoteForm
    template_name = 'formularios/create-quote.html'
    success_url = reverse_lazy('quotes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nueva Cotización'
        context['buttom'] = 'Crear Registro'
        context['date'] = datetime.date.today()
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#listar Cotizaciones
class QuoteListView(ListView):
    model = Quotes
    template_name = 'listado/quotes.html'
    ordering = ['-id']

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#actualizar cotizaciones
class QuoteUpdateView(UpdateView):
    model = Quotes
    form_class = QuoteForm
    template_name = 'formularios/create-quote.html'
    success_url = reverse_lazy('quotes')

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Cotización'
        context["buttom"] = 'Actualizar Registro'
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#crear pagos
class PaymentCreateView(CreateView):
    model = Payments
    form_class = PayForm
    template_name = 'formularios/create-pay.html'
    success_url = reverse_lazy('payments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Pago'
        context['buttom'] = 'Crear Registro'
        context['date'] = datetime.date.today()
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#actualizar pago
class PaymentUpdateView(UpdateView):
    model = Payments
    form_class = PayForm
    template_name = 'formularios/create-pay.html'
    success_url = reverse_lazy('payments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Pago'
        context['buttom'] = 'Actualizar Registro'
        context['date'] = datetime.date.today()
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#LISTAR PAGOS
class PaymentListView(ListView):
    model = Payments
    template_name = 'listado/payments.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#crear PRELIMINARES
class PreliminaryCreateView(CreateView):
    model = Preliminary
    form_class = PreliminaryForm
    template_name = 'formularios/create-preliminary.html'
    success_url = reverse_lazy('preliminaries')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nuevo Registro de Preliminar'
        context['buttom'] = 'Crear Registro'
        context['date'] = datetime.date.today()
        return context
    
    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#LISTAR PRELIMINAR
class PreliminaryListView(ListView):
    model = Preliminary
    template_name = 'listado/preliminares.html'

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#UPDATE PRELIMINARY
class PreliminaryUpdateView(UpdateView):
    model = Preliminary
    form_class = PreliminaryForm
    template_name = 'formularios/create-preliminary.html'
    success_url = reverse_lazy('preliminaries')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Preliminar'
        context["buttom"] = 'Actualizar Registro'
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

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#crear Correciones
class CorrectionCreateView(CreateView):
    model= Corrections
    form_class = CorregirAPT
    template_name = 'formularios/create-correction.html'
    success_url = reverse_lazy('corrections')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Nueva Correción'
        context['buttom'] = 'Crear Registro'
        return context

    "to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#listar correciones
class CorrectionListView(ListView):
    model = Corrections
    template_name = 'listado/corrections.html'

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

#actualizad correciones
class CorreccionUpdateView(UpdateView):
    model = Corrections
    form_class = CorregirAPT
    template_name = 'formularios/create-correction.html'
    success_url = reverse_lazy('corrections')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Actualizar Registro de Correción'
        context['buttom'] = 'Actualizar Registro'
        return context

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



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

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#listar replanteos
class ReplantListView(ListView):
    model = Replant
    template_name = 'listado/replant.html'

    #"to keep secure the view"
    @method_decorator(login_required(login_url='login'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    #"to keep secure the view"
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
    campo = FieldSurvey.objects.get(solicitud_id_id = id)
    solicitud = Solicitudes.objects.get(quote_id = id)
    preliminar = Preliminary.objects.get(quote_id = id)
    template=''
    service=''
    service2 = ''
    service3 = ''
    
    if servicio == 'Informe':
        service = Quotes.objects.get(id=id).solicitudReport.all() 
        template='detalles/detail-report.html'
    elif servicio == 'Plano Catastrado':
        service = Quotes.objects.get(id=id).solicitudCadastral.all() 
        template='detalles/detail-catastro.html'
    elif servicio == 'Replanteo':
        service = Quotes.objects.get(id=id).solicitudReplant.all() 
        template='detalles/detail-replant.html'
    elif servicio == 'Curvas de Nivel':
        service = Quotes.objects.get(id=id).solicitudLevel.all() 
        template='detalles/detail-level.html' 
    elif servicio == 'Curvas de Nivel--Replanteo':
        service = Quotes.objects.get(id=id).solicitudLevel.all()
        service2 = Quotes.objects.get(id=id).solicitudReplant.all()
        template = 'detalles/detail-level-replant.html'
    elif servicio == 'Informe--Curvas de Nivel':
        service = Quotes.objects.get(id=id).solicitudReport.all()
        service2 = Quotes.objects.get(id=id).solicitudLevel.all()
        template = 'detalles/detail-report-level.html'
    elif servicio == 'Informe--Replanteo':
        service = Quotes.objects.get(id=id).solicitudReport.all()
        service2 = Quotes.objects.get(id=id).solicitudReplant.all()
        template = 'detalles/detail-report-replant.html'
    elif servicio == 'Informe--Catastro':
        service = Quotes.objects.get(id=id).solicitudReport.all()
        service2 = Quotes.objects.get(id=id).solicitudCadastral.all()
        template = 'detalles/detail-report-catastro.html'
    elif servicio == 'Informe--Catastro--Curvas de Nivel':
        service = Quotes.objects.get(id=id).solicitudReport.all()
        service2 = Quotes.objects.get(id=id).solicitudCadastral.all()
        service3 = Quotes.objects.get(id=id).solicitudLevel.all()
        template = 'detalles/detail-report-catastro-curves.html'
    elif servicio == 'Informe--Replanteo--Curvas de Nivel':
        service = Quotes.objects.get(id=id).solicitudReport.all()
        service2 = Quotes.objects.get(id=id).solicitudReplant.all()
        service3 = Quotes.objects.get(id=id).solicitudLevel.all()
        template = 'detalles/detail-report-replant-curves.html'

        
    return render(request, template, {'solicitud':solicitud, 'service':service, 'service2':service2, 'service3':service3, 'campo': campo, 'preliminar':preliminar})

#puedo usar una vista donde se agrega al context de los modelos Informes, Catastro, Reporte, Replanteo, Lev Campo y Solicitudes
#se debe filtrar id.informe = id.

#hacer pendientes en pagína de inicio que redirija a cada estatus
#pendiente, link a resumen 