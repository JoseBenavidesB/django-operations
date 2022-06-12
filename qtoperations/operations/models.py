from django.db import models
from django.core.validators import MinValueValidator
import datetime

from django.contrib.auth.models import Group
from django.db.models.deletion import DO_NOTHING


# Create your models here

#DEPARTAMENTOS
""" class Department(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Departamento:", unique=True, help_text="Escriba el nombre del departamento")
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        

    def __str__(self):
        return f'{self.name}' """

#ocupaciones
class Ocupations(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False, unique=True, verbose_name="Nombre de Ocupación", help_text="Escriba el nombre de la ocupación")

    class Meta:
        verbose_name='Ocupación en QT'
        verbose_name_plural = 'Ocupaciones QT'

    def __str__(self):
        return self.name

#empleados
class Employees(models.Model):

    name= models.CharField(max_length=25, verbose_name='Nombre', blank=False, null=False)
    last_name = models.CharField(max_length=50, verbose_name='Apellidos', blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Telefono', blank=True, null=False)
    ocupation = models.ForeignKey(Ocupations, on_delete=models.DO_NOTHING, verbose_name='Ocupación', null=True)
    department = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True, verbose_name="Departamento")

    class Meta:
        verbose_name= 'Colaborador en QT'
        verbose_name_plural = 'Colaboradores QT'
        

    def __str__(self):
        return f'{self.name}'

#clientes
class Customers(models.Model):
    nacionalidad = [
        ('Extranjero', 'Extranjero'),
        ('Costarricense', 'Costarricense')
    ]

    name = models.CharField(max_length=200, verbose_name='Nombre', null=False)
    cedula = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Cédula o pasaporte")
    nacionalidad = models.CharField(max_length=20, choices=nacionalidad, null=True, blank=False, verbose_name="Nacionalidad")
    direction = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección")
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name="Provincia")
    canton = models.CharField(max_length=30, null=True, blank=True, verbose_name="Cantón")
    district = models.CharField(max_length=30, null=True, blank=True, verbose_name="Distrito")
    phoneNumber = models.CharField(max_length=40, verbose_name='Numero telefonico', blank=True, null=True)
    mobileNumber = models.CharField(max_length=40, verbose_name='Numero Celular', blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    company = models.BooleanField(verbose_name="Es una empresa?", null=True)

    class Meta:
        verbose_name='Cliente / Empresa'
        verbose_name_plural='Clientes / Empresas'

    def __str__(self):
        return f'{self.name}'

#empresas
class Sub_customers(models.Model):
    nacionalidad = [
        ('Extranjero', 'Extranjero'),
        ('Residente', 'Residente'),
        ('Costarricense', 'Costarricense')
    ]

    name = models.CharField(max_length=200, verbose_name='Nombre', null=False)
    cedula = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Cédula o pasaporte")
    nacionalidad = models.CharField(max_length=20, choices=nacionalidad, null=True, blank=False, verbose_name="Nacionalidad")
    phoneNumber = models.CharField(max_length=40, verbose_name='Numero telefonico', blank=True, null=True)
    mobileNumber = models.CharField(max_length=40, verbose_name='Numero Celular', blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    company = models.ForeignKey(Customers, default=False, null=True, blank=True, on_delete=DO_NOTHING, verbose_name="Empresa")

    class Meta:
        verbose_name= 'Colaborador de Empresa'
        verbose_name_plural = 'Colaboradores de Empresas'
        

    def __str__(self):
        return f'{self.name}' #con esto puedo manipular para que se presente SF-0003

#servicios
class Services(models.Model):
    typeService = models.CharField(max_length=40, verbose_name="Tipo Servicio", unique=True)

    class Meta:
        verbose_name= 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return str(self.typeService)

#COTIZACIONES
class Quotes(models.Model):
    estados = [
        ('Pendiente Revisión', 'Pendiente Revisión'),
        ('Enviado al Cliente', 'Enviado al Cliente'),
        ('Pendiente de Envio', 'Pendiente de Envio'),
        ('Rechazado', 'Rechazado'),
        ('Aprobada', 'Aprobada')
    ]
    description = models.CharField(max_length=100, null=True, blank=False, verbose_name="Descripción", help_text="Descripción de la cotización")
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, null=True, verbose_name='Servicio')
    plan = models.URLField(blank=True, verbose_name='Plano', max_length=200, help_text="Link del plano, por favor")
    finca = models.CharField(max_length=100, null=True, blank=True, verbose_name="Número de Finca", help_text="Número de folio real")
    area = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Área del proyecto", blank=True, null=True)
    location = models.CharField(max_length=50, verbose_name='Localización', help_text="Escriba la ubicación del lote", blank=True, null=True)
    customer = models.ForeignKey(Customers, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name="Cliente", related_name="quote_customer")
    contact = models.CharField(max_length=50, null=True, blank=True, verbose_name="Contacto", help_text="Escriba el nombre del contacto")
    date_request = models.DateField(null=True, blank=True, verbose_name="Fecha de solicitud", help_text= "Colocar Fecha dd/mm/año")
    date_send = models.DateField(null=True, blank=True, verbose_name="Cotización enviada el:", help_text= "Colocar Fecha dd/mm/año")
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en $",blank=True, null=True, help_text="Digite el monto (máximo 2 decimales)")
    amount2 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en ¢",blank=True, null=True, help_text="Digite el monto (máximo 2 decimales)")
    date_answer = models.DateField(null=True, blank=True, verbose_name="Fecha de aprobación o rechazo:", help_text= "Colocar Fecha dd/mm/año")
    final_customer = models.ForeignKey(Sub_customers, null=True, blank=True, on_delete=models.DO_NOTHING, verbose_name="En caso de ser Empresa, solicitado por:")
    preliminary_date = models.DateField(null=True, blank=True, verbose_name="Fecha preliminar:", help_text= "Colocar Fecha dd/mm/año")
    internal_review = models.DateField(null=True, blank=True, verbose_name="Revisión interna:", help_text= "Colocar Fecha dd/mm/año")
    delivery_date = models.DateField(null=True, blank=True, verbose_name="Fecha de entrega:", help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=50, null=True, verbose_name="Estatus", choices=estados)
    
    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        ordering = ['-id']

    def __str__(self):
        return f'QT-{self.customer.id}-{self.id}|[{self.description}]'

#pago
class Payments(models.Model):
    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, verbose_name="Cotización", related_name="payment_quote")
    bill1 = models.CharField(max_length= 20, null=True, blank=True, verbose_name="Número de factura #1")
    amount_bill1 = models.DecimalField(max_digits=9, null=True, blank=True, decimal_places=2, verbose_name="Monto en $", help_text="Digite el monto (máximo 2 decimales)")
    date_bill1 = models.DateField(null=True, blank=True, verbose_name="Fecha de 1 factura", help_text= "Colocar Fecha dd/mm/año") 
    bill2 = models.CharField(max_length= 20, null=True, blank=True, verbose_name="Número de factura #2")
    amount_bill2 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en $", blank=True, null=True, help_text="Digite el monto (máximo 2 decimales)s")
    date_bill2 = models.DateField(null=True, blank=True, verbose_name="Fecha de 2 factura", help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
   
    "nombre, identidicacion, correo, direccion, provincia, distrito, canton, cotizacion, precio, fecha cotizacion, costo, factura, numero de factura, fecha, monto, deposito, "
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ['-id']

    def __str__(self):
        return f'Pago de {self.quote}'

#preliminar
class Preliminary(models.Model):
    estados = [
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
        ('En Proceso', 'En proceso'),
    ]

    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Cotización')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="preliminary_assigned")
    schedule_service = models.DateField(null=True, blank=True, verbose_name="Servicio agendado")
    locationMark = models.DateField(null=True, blank=True, verbose_name="Marca de Ubicación", help_text= "Colocar Fecha dd/mm/año")
    googleMaps = models.DateField(null=True, blank=True, verbose_name="GoogleMap")
    google_to_group = models.DateField(null=True, blank=True, verbose_name="Google enviado al Grupo")
    downloaded_plans = models.DateField(null=True, blank=True, verbose_name="Descarga de Planos")
    draw_plans = models.DateField(null=True, blank=True, verbose_name="Dibujo de Planos")
    sketch = models.DateField(null=True, blank=True, verbose_name="Croquis Preliminares")
    document = models.DateField(null=True, blank=True, verbose_name="Modificación preliminar del documento")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, null=True, verbose_name="Estatus", default='Pendiente', choices=estados)

    class Meta:
        verbose_name = 'Preliminar'
        verbose_name_plural = 'Preliminares'
        ordering = ['-id']

    def __str__(self):
        return f'Preliminar de {self.quote}'

#solicitudes
class Solicitudes(models.Model):

    estados = [
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
        ('En proceso', 'En proceso'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]

    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Descripción')
    #customer_id = models.ForeignKey(Customers, on_delete= models.SET_NULL, null=True, verbose_name='Cliente')
    #service_id = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, verbose_name='Servicio')
    #contact = models.CharField(max_length=50, verbose_name='Contacto', null=True, blank=True)
    #deliveryDate = models.DateField(blank=True, null=True ,verbose_name='Fecha Entrega', help_text= "Colocar Fecha dd/mm/año")
    #plan = models.URLField(blank=True, verbose_name='Plano', max_length=200, help_text="Link del plano, por favor")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados,default='Pendiente', verbose_name="Estado")
    
    
    #survey = models.BooleanField(default=True, verbose_name='Necesita Lev Campo?')
    #validators=[MinValueValidator(datetime.date.today)] para validar que la fecha minima
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['-id']

        #event tiene FK a venueob, 

    def __str__(self):
        return f' Solicitud {self.quote}'

        """for access Reportes = Reports.objects.select_related('nombre del campo en este caso solicitud_id')
        luego para acceder a los valores del otro se utiliza:
        i.solicitud_id.status"""

#levantamiento de campo
class FieldSurvey(models.Model):
    estados = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]    
    solicitud_id= models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='solicitudField')
    contact = models.DateField(null=True, blank=True, verbose_name= "Contactar sitio")
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name="Asignacion General a:", related_name="fieldsurvey_assigned")
    proposedDate = models.DateField(blank=True, null=True, verbose_name='Fecha Propuesta', help_text= "Colocar Fecha dd/mm/año")
    fieldSurveyDate = models.DateField(blank=True, null=True, verbose_name='Fecha Lev. Campo', help_text= "Colocar Fecha dd/mm/año")
    gnss_survey = models.ForeignKey(Employees, null=True, blank=True, verbose_name='Uso de GNSS', on_delete=DO_NOTHING, related_name='survey_gnss')
    station_survey = models.ForeignKey(Employees, null=True, blank=True, verbose_name='Uso de estación',on_delete=DO_NOTHING, related_name='survey_station')
    fly_drone = models.ForeignKey(Employees, null=True, blank=True, verbose_name='Uso de Drone',on_delete=DO_NOTHING, related_name='survey_drone')
    conclusionDate = models.DateField(blank=True, null=True, verbose_name='Fecha de Conclusión', help_text= "Colocar Fecha dd/mm/año")
    downloadedData = models.DateField(blank=True, null=True, verbose_name='Fecha Descarga Datos', help_text= "Colocar Fecha dd/mm/año")
    armed_information = models.DateField(blank=True, null=True, verbose_name='Info. armada', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados, default='Pendiente', verbose_name='Estado')

    class Meta:    
        verbose_name='Levantamiento de Campo'
        verbose_name_plural='Levantamientos de Campo'
        ordering = ['-id']

    def __str__(self):
        return f'Lev Campo {self.solicitud_id}'

#DIBUJO la idea es meter el dibujo a cada servicio en la tabla donde la solicitud sea igual tanto para dibujo como levCampo, informe, catastro
""" class Draw(models.Model):
    estados= {
        ('sin_concluir', 'Sin concluir'),
        ('finalizado', 'Finalizado' )
    }

    solicitud = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudDraw')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="draw_assigned")
    armed_information = models.DateField(null=True, blank=True, verbose_name='Lev armado', help_text= "Colocar Fecha dd/mm/año")
    aligned_plan = models.DateField(null=True, blank=True, verbose_name='Plano Alineado', help_text= "Colocar Fecha dd/mm/año")
    sketch = models.DateField(null=True, blank=True, verbose_name="Croquis", help_text= "Colocar Fecha dd/mm/año")
    review = models.DateField(null=True, blank=True, verbose_name="Revisado", help_text= "Colocar Fecha dd/mm/año")
    status = models.CharField(max_length=15, choices=estados, default='Sin concluir', verbose_name='Estado')

    class Meta:
        verbose_name = 'Dibujo'
        verbose_name_plural = 'Dibujos'
    
    def __str__(self):
        return f'Dibujo|| {self.solicitud}' """


#informes
class Reports(models.Model):
    estados = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]
    solicitud_id= models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudReport')
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas', help_text= "Colocar Fecha dd/mm/año")
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Croquis asignado a:", related_name="reports_assigned")
    sketch = models.DateField(null=True, blank=True, verbose_name='Croquis', help_text= "Colocar Fecha dd/mm/año")
    process_fly = models.DateField(null=True, blank=True, verbose_name='Vuelo procesado', help_text= "Colocar Fecha dd/mm/año")
    drafting = models.DateField(blank=True, null=True, verbose_name='Redacción del Doc.', help_text= "Colocar Fecha dd/mm/año")
    assigned_2 = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Redacción asignado a:", related_name="reports_assigned2")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión', help_text= "Colocar Fecha dd/mm/año")
    finalReview = models.DateField(blank=True, null=True, verbose_name='Revisón Final', help_text= "Colocar Fecha dd/mm/año")
    submittedReport = models.DateField(blank=True, null=True, verbose_name='Reporte enviado el:', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados, default='En Proceso', verbose_name='Estado')

    class Meta:    
        verbose_name='Informe'
        verbose_name_plural='Informes'
        ordering = ['-id']

    def __str__(self):
        return f'Informe||{self.solicitud_id}'


#curvas de nivel
class levelCurves(models.Model):

    estados = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]
    solicitud_id= models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudLevel')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="levelcurves_assigned")
    process_fly = models.DateField(null=True, blank=True, verbose_name='Vuelo procesado', help_text= "Colocar Fecha dd/mm/año")
    draw = models.DateField(blank=True, null=True, verbose_name='Dibujo', help_text= "Colocar Fecha dd/mm/año")
    presentation = models.DateField(blank=True, null=True, verbose_name='Presentación', help_text= "Colocar Fecha dd/mm/año")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión', help_text= "Colocar Fecha dd/mm/año")
    submittedCurves = models.DateField(blank=True, null=True, verbose_name='Curvas entregadas el:', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados, default='En Proceso', verbose_name='Estado')


    class Meta:    
        verbose_name='Curvas de Nivel'
        verbose_name_plural='Curvas de Nivel'
        ordering = ['-id']

    def __str__(self):
        return f'Curvas de Nivel||{self.solicitud_id}'


#catastro 
class CadastralPlans(models.Model):
    estados = [
        ('Sin Tramitar', 'Sin Tramitar'),
        ('Subido al APT', 'Subido al APT'),
        ('Rechazado', 'Rechazado'),
        ('Cancelado', 'Cancelado'),
        ('Apelación', 'Apelación'),
        ('Oposicion', 'Oposicion'),
        ('Inscrito', 'Inscrito'),
    ]

    solicitud_id= models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudCadastral')
    protocolo =  models.DateField(blank=True, null=True, verbose_name='Protocolo lleno', help_text= "Colocar Fecha dd/mm/año")
    signed_protocol =  models.DateField(blank=True, null=True, verbose_name='Protocolo comprado', help_text= "Colocar Fecha dd/mm/año")
    process_fly = models.DateField(null=True, blank=True, verbose_name='Vuelo procesado', help_text= "Colocar Fecha dd/mm/año")
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="cadastralplans_assigned")
    draw_plan =  models.DateField(blank=True, null=True, verbose_name='Planos dibujados', help_text= "Colocar Fecha dd/mm/año")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión', help_text= "Colocar Fecha dd/mm/año")
    timbres = models.DateField(blank=True, null=True, verbose_name='Timbres comprados', help_text= "Colocar Fecha dd/mm/año")
    apt =  models.DateField(blank=True, null=True, verbose_name='APT lleno', help_text= "Colocar Fecha dd/mm/año")
    uploadedAPT = models.DateField(blank=True, null=True, verbose_name='Subido APT', help_text= "Colocar Fecha dd/mm/año")
    visado =  models.DateField(blank=True, null=True, verbose_name='Visado', help_text= "Colocar Fecha dd/mm/año")
    minute_review =  models.DateField(blank=True, null=True, verbose_name='Revisión Minuta', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados, default='Sin Tramitar', verbose_name="Estado")
    #aqui deberia ser, estadus: pendiente, revision, cancelado, rebotado, inscrito
    class Meta:
        verbose_name = 'Plano Catastrado'
        verbose_name_plural = 'Planos Catastrados'
        ordering = ['-id']

    def __str__(self):
        return f'PlCt||{self.solicitud_id}'

#correciones catastro
class Corrections(models.Model):
    cadastral_id= models.ForeignKey(CadastralPlans, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Catastro')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="corrections_assigned")
    downloadedMinute = models.DateField(blank=True, null=True, verbose_name='Minuta Descargada', help_text= "Colocar Fecha dd/mm/año") 
    errorReview = models.DateField(blank=True, null=True, verbose_name='Revisión de Errores', help_text= "Colocar Fecha dd/mm/año")
    corrections = models.DateField(blank=True, null=True, verbose_name='Correciones', help_text= "Colocar Fecha dd/mm/año")
    uploadedAPT = models.DateField(blank=True, null=True, verbose_name='Subido APT', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )

    class Meta:
        verbose_name = 'Correción'
        verbose_name_plural = 'Correciones'
        ordering = ['-id']

    def __str__(self):
        return f'Correciones||{self.cadastral_id}'    

#replanteo 
class Replant(models.Model):
    estados = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]

    solicitud_id= models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudReplant')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="replant_assigned")
    armed_info = models.DateField(blank=True, null=True, verbose_name='Info. Armada', help_text= "Colocar Fecha dd/mm/año")
    process_fly = models.DateField(null=True, blank=True, verbose_name='Vuelo procesado', help_text= "Colocar Fecha dd/mm/año")
    files_replant = models.DateField(blank=True, null=True, verbose_name='Archivos de Replanteo', help_text= "Colocar Fecha dd/mm/año") 
    replantingPoints = models.DateField(blank=True, null=True, verbose_name='Rep. Puntos en sitio', help_text= "Colocar Fecha dd/mm/año")
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas', help_text= "Colocar Fecha dd/mm/año")
    drafting = models.DateField(blank=True, null=True, verbose_name='Redacción del Doc.', help_text= "Colocar Fecha dd/mm/año")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión', help_text= "Colocar Fecha dd/mm/año")
    submittedReport = models.DateField(blank=True, null=True, verbose_name='Reporte entregado el:', help_text= "Colocar Fecha dd/mm/año")
    note = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Comentario' )
    status = models.CharField(max_length=15, choices=estados, default='Sin Tramitar', verbose_name="Estado")    

    class Meta:
        verbose_name = 'Replanteo'
        verbose_name_plural = 'Replanteos'
        ordering = ['-id']
    
    def __str__(self):
        return f'Replanteo||{self.solicitud_id}'



'''nota, puedo poner lev de campo y que este le lleve a la solicitud, 
que el informe me lleve al estado del lev de campo
es decir, que sean consultas inversas con botones, esto se hará en las vista
y se agregará al context data, por lo tanto, modificar el metodo '''


"""model blog
model author

model entry tiene FK a Blog y MANY a Author

EL MODELO ENTRY PUEDE ACCEDER A LAS PROPIEDADES
DEL MODELO blog USANDO __, ej:
Entry.objects.filter(blog__name='beatles)"""

#inlinecss django
#decoulple django