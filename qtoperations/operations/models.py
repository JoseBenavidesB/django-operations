from django.db import models
from django.core.validators import MinValueValidator
import datetime


# Create your models here

#DEPARTAMENTOS
class Department(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Departamento:", unique=True, help_text="Escriba el nombre del departamento")
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f'{self.name}'

#ocupaciones
class Ocupations(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False, unique=True, verbose_name="Nombre de Ocupación", help_text="Escriba el nombre de la ocupación")

    class Meta:
        verbose_name='Ocupación'
        verbose_name_plural = 'Ocupaciones'

    def __str__(self):
        return self.name

#empleados
class Employees(models.Model):

    name= models.CharField(max_length=25, verbose_name='Nombre', blank=False, null=False)
    last_name = models.CharField(max_length=50, verbose_name='Apellidos', blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=20, verbose_name='Telefono', blank=True, null=False)
    ocupation = models.ForeignKey(Ocupations, on_delete=models.DO_NOTHING, verbose_name='Ocupación', null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=True, verbose_name="Departamento")

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'{self.name}'

#empresas
class Empresas(models.Model):

    name = models.CharField(max_length=200, verbose_name='Empresa', unique=True)
    prefix = models.CharField(max_length=10, verbose_name='Prefijo', blank=True, null=True, unique=True)

    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return (self.prefix) #con esto puedo manipular para que se presente SF-0003

#clientes
class Customers(models.Model):
    nacionalidad = [
        ('estranjero', 'Estranjero'),
        ('residente', 'Residente'),
        ('costarricense', 'Costarricense')
    ]

    name = models.CharField(max_length=100, verbose_name='Nombre', null=False)
    lastName = models.CharField(max_length=100, verbose_name='Apellidos', blank=True, null=True)
    cedula = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name="Cédula o pasaporte")
    nacionalidad = models.CharField(max_length=20, choices=nacionalidad, null=True, blank=False, verbose_name="Nacionalidad")
    direction = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección")
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name="Provincia")
    canton = models.CharField(max_length=30, null=True, blank=True, verbose_name="Cantón")
    district = models.CharField(max_length=30, null=True, blank=True, verbose_name="Distrito")
    phoneNumber = models.CharField(max_length=40, verbose_name='Numero telefonico', blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True, unique=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return f'{self.name}({self.empresa})'

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
        ('PR', 'Pendiente Revisión'),
        ('EC', 'Enviado al Cliente'),
        ('PE', 'Pendiente de Envio'),
        ('R', 'Rechazado'),
        ('A', 'Aprobada')
    ]
    description = models.CharField(max_length=100, null=True, blank=False, verbose_name="Descripción", help_text="Descripción de la cotización")
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING, null=True, verbose_name='Servicio')
    customer = models.ForeignKey(Customers, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name="Cliente", related_name="quote_customer")
    contact = models.CharField(max_length=50, null=True, blank=True, verbose_name="Contacto", help_text="Escriba el nombre del contacto")
    amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en $", help_text="Digite el monto con 2 decimales")
    amount2 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en ¢",blank=True, null=True, help_text="Digite el monto con 2 decimales")
    date = models.DateField(auto_now_add=True, verbose_name="Fecha de cotización") 
    final_customer = models.ForeignKey(Customers, null=True, blank=False, on_delete=models.DO_NOTHING, verbose_name="Cliente Final")
    status = models.CharField(max_length=15, null=True, verbose_name="Estatus", choices=estados, default='PR')
    
    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'

    def __str__(self):
        return f'{self.id}-{self.description}||{self.final_customer}'

#pago
class Payments(models.Model):
    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, verbose_name="Cotización", related_name="payment_quote")
    bill1 = models.CharField(max_length= 20, null=True, blank=True, verbose_name="Número de factura #1")
    amount_bill1 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en $", help_text="Digite el monto con 2 decimales")
    date_bill1 = models.DateField(null=True, blank=True, verbose_name="Fecha de 1 factura")
    bill2 = models.CharField(max_length= 20, null=True, blank=True, verbose_name="Número de factura #2")
    amount_bill2 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Monto en $", blank=True, null=True, help_text="Digite el monto con 2 decimales")
    date_bill2 = models.DateField(null=True, blank=True, verbose_name="Fecha de 2 factura")

    "nombre, identidicacion, correo, direccion, provincia, distrito, canton, cotizacion, precio, fecha cotizacion, costo, factura, numero de factura, fecha, monto, deposito, "
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f'Pago de {self.quote}'

#preliminar
class Preliminary(models.Model):
    estados = [
        ('pendiente', 'Pendiente'),
        ('finalizado', 'Finalizado'),
        ('atrasado', 'Atrasado'),
        ('cancelado', 'Cancelado'),
        ('enProceso', 'En proceso'),
    ]

    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Cotización')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="preliminary_assigned")
    locationMark = models.DateField(null=True, blank=True, verbose_name="Marca de Ubicación")
    googleMaps = models.DateField(null=True, blank=True, verbose_name="GoogleMap")
    sketch = models.DateField(null=True, blank=True, verbose_name="Croquis Preliminares")
    document = models.DateField(null=True, blank=True, verbose_name="Modificación preliminar del documento")
    status = models.CharField(max_length=15, null=True, verbose_name="Estatus", choices=estados)

    class Meta:
        verbose_name = 'Preliminar'
        verbose_name_plural = 'Preliminares'

    def __str__(self):
        return f'Preliminar de {self.quote}'

#solicitudes
class Solicitudes(models.Model):

    estados = [
        ('Pendiente', 'Pendiente'),
        ('Finalizado', 'Finalizado'),
        ('En proceso', 'En proceso'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]

    quote = models.ForeignKey(Quotes, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Descripción')
    customer_id = models.ForeignKey(Customers, on_delete= models.SET_NULL, null=True, verbose_name='Cliente')
    service_id = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, verbose_name='Servicio')
    contact = models.CharField(max_length=50, verbose_name='Contacto', null=True, blank=True)
    deliveryDate = models.DateField(validators=[MinValueValidator(datetime.date.today)], blank=True, null=True ,verbose_name='Fecha Entrega')
    plan = models.ImageField(default='null', verbose_name='Plano', upload_to='planos')
    status = models.CharField(max_length=15, choices=estados,default='Pendiente', verbose_name="Estado")
    location = models.CharField(max_length=50, verbose_name='Localización', help_text="Escriba la ubicación del lote", blank=True, null=True)
    area = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Área", blank=True, null=True)
    #survey = models.BooleanField(default=True, verbose_name='Necesita Lev Campo?')

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        #event tiene FK a venueob, 

    def __str__(self):
        return f' Solicitud {self.quote}'

        """for access Reportes = Reports.objects.select_related('nombre del campo en este caso solicitud_id')
        luego para acceder a los valores del otro se utiliza:
        i.solicitud_id.status"""

#levantamiento de campo
class FieldSurvey(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='solicitudField')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="fieldsurvey_assigned")
    proposedDate = models.DateField(blank=True, null=True, verbose_name='Fecha Propuesta')
    fieldSurveyDate = models.DateField(blank=True, null=True, verbose_name='Fecha Lev. Campo')
    conclusionDate = models.DateField(blank=True, null=True, verbose_name='Fecha de Conclusión')
    downloadedData = models.DateField(blank=True, null=True, verbose_name='Fecha Descarga Datos')
    armed_information = models.DateField(blank=True, null=True, verbose_name='Info. armada')

    class Meta:    
        verbose_name='Levantamiento de Campo'
        verbose_name_plural='Levantamientos de Campo'

    def __str__(self):
        return f'Lev Campo {self.solicitud_id}'

#DIBUJO la idea es meter el dibujo a cada servicio en la tabla donde la solicitud sea igual tanto para dibujo como levCampo, informe, catastro
class Draw(models.Model):
    estados= {
        ('sin_concluir', 'Sin concluir'),
        ('finalizado', 'Finalizado' )
    }

    solicitud = models.ForeignKey(Solicitudes, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudDraw')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="draw_assigned")
    armed_information = models.DateField(null=True, blank=True, verbose_name='Lev armado')
    aligned_plan = models.DateField(null=True, blank=True, verbose_name='Plano Alineado')
    sketch = models.DateField(null=True, blank=True, verbose_name="Croquis")
    review = models.DateField(null=True, blank=True, verbose_name="Revisado")
    status = models.CharField(max_length=15, choices=estados, default='Sin concluir', verbose_name='Estado')

    class Meta:
        verbose_name = 'Dibujo'
        verbose_name_plural = 'Dibujos'
    
    def __str__(self):
        return f'Dibujo|| {self.solicitud}'


#informes
class Reports(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudReport')
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas')
    sketch = models.DateField(null=True, blank=True, verbose_name='Croquis')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="reports_assigned")
    drafting = models.DateField(blank=True, null=True, verbose_name='Redacción del Doc.')
    assigned_2 = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="reports_assigned2")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    finalReview = models.DateField(blank=True, null=True, verbose_name='Revisón Final')
    submittedReport = models.DateField(blank=True, null=True, verbose_name='Reporte enviado el:')

    class Meta:    
        verbose_name='Informe'
        verbose_name_plural='Informes'

    def __str__(self):
        return f'Informe||{self.solicitud_id}'


#curvas de nivel
class levelCurves(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudLevel')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="levelcurves_assigned")
    draw = models.DateField(blank=True, null=True, verbose_name='Dibujo')
    presentation = models.DateField(blank=True, null=True, verbose_name='Presentación')
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    submittedCurves = models.DateField(blank=True, null=True, verbose_name='Curvas entregadas el:')

    class Meta:    
        verbose_name='Curvas de Nivel'
        verbose_name_plural='Curvas de Nivel'

    def __str__(self):
        return f'Curvas de Nivel||{self.solicitud_id}'


#catastro 
class CadastralPlans(models.Model):
    estados = [
        ('Sin Tramitar', 'Sin Tramitar'),
        ('Subido', 'Subido al APT'),
        ('Rechazado', 'Rechazado'),
        ('Cancelado', 'Cancelado'),
        ('Apelación', 'Apelación'),
        ('Oposicion', 'Oposicion'),
        ('Inscrito', 'Inscrito'),
    ]

    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudCadastral')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="cadastralplans_assigned")
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    timbres = models.DateField(blank=True, null=True, verbose_name='Timbres comprados')
    uploadedAPT = models.DateField(blank=True, null=True, verbose_name='Subido APT')
    status = models.CharField(max_length=15, choices=estados, default='Sin Tramitar', verbose_name="Estado")
    #aqui deberia ser, estadus: pendiente, revision, cancelado, rebotado, inscrito
    class Meta:
        verbose_name = 'Plano Catastrado'
        verbose_name_plural = 'Planos Catastrados'

    def __str__(self):
        return f'PlCt||{self.solicitud_id}'

#correciones catastro
class Corrections(models.Model):
    cadastral_id= models.ForeignKey(CadastralPlans, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Catastro')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="corrections_assigned")
    downloadedMinute = models.DateField(blank=True, null=True, verbose_name='Minuta Descargada') 
    errorReview = models.DateField(blank=True, null=True, verbose_name='Revisión de Errores')
    corrections = models.DateField(blank=True, null=True, verbose_name='Correciones')
    uploadedAPT = models.DateField(blank=True, null=True, verbose_name='Subido APT')

    class Meta:
        verbose_name = 'Correción'
        verbose_name_plural = 'Correciones'

    def __str__(self):
        return f'Correciones||{self.cadastral_id}'    

#replanteo 
class Replant(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud', related_name='solicitudReplant')
    assigned_to = models.ForeignKey(Employees, on_delete=models.DO_NOTHING, null=True, blank=False, verbose_name="Asignado a:", related_name="replant_assigned")
    armed_info = models.DateField(blank=True, null=True, verbose_name='Info. Armada')
    files_replant = models.DateField(blank=True, null=True, verbose_name='Archivos de Replanteo') 
    replantingPoints = models.DateField(blank=True, null=True, verbose_name='Rep. Puntos en sitio')
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas')
    drafting = models.DateField(blank=True, null=True, verbose_name='Redacción del Doc.')
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    submittedReport = models.DateField(blank=True, null=True, verbose_name='Reporte entregado el:')

    class Meta:
        verbose_name = 'Replanteo'
        verbose_name_plural = 'Replanteos'
    
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