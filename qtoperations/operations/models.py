from django.db import models
from django.core.validators import MinValueValidator
import datetime

# Create your models here.

#empresas
class Empresas(models.Model):

    name = models.CharField(max_length=200, verbose_name='Empresa')
    prefix = models.CharField(max_length=10, verbose_name='Prefijo', blank=True, null=True)

    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return (self.prefix) #con esto puedo manipular para que se presente SF-0003

#clientes
class Customers(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', null=False)
    lastName = models.CharField(max_length=100, verbose_name='Apellidos', blank=True, null=True)
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
    typeService = models.CharField(max_length=40, verbose_name="Tipo Servicio")

    class Meta:
        verbose_name= 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return str(self.typeService)

#solicitudes
class Solicitudes(models.Model):

    estados = [
        ('Pendiente', 'Pendiente'),
        ('Entregado', 'Entregado'),
        ('Atrasado', 'Atrasado'),
        ('Cancelado', 'Cancelado'),
    ]

    name = models.CharField(max_length=150, verbose_name='Solicitudes', null=False, blank=False)
    customer_id = models.ForeignKey(Customers, on_delete= models.SET_NULL, null=True, verbose_name='Cliente')
    service_id = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, verbose_name='Servicio')
    contact = models.CharField(max_length=50, verbose_name='Contacto', null=True, blank=True)
    deliveryDate = models.DateField(validators=[MinValueValidator(datetime.date.today)], blank=True, null=True ,verbose_name='Fecha Entrega')
    plan = models.ImageField(default='null', verbose_name='Plano', upload_to='planos')
    status = models.CharField(max_length=15, choices=estados,default='Pendiente', verbose_name="Estado")
    survey = models.BooleanField(default=True, verbose_name='Necesita Lev Campo?')

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        #event tiene FK a venueob, 

    def __str__(self):
        return f'{self.id}-{self.name} [{self.customer_id}]'

#levantamiento de campo
class FieldSurvey(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud')
    tentativeDate = models.DateField(blank=True, null=True, verbose_name='Fecha Tentativa')
    proposedDate = models.DateField(blank=True, null=True, verbose_name='Fecha Propuesta')
    fieldSurveyDate = models.DateField(blank=True, null=True, verbose_name='Fecha Lev. Campo')
    conclusionDate = models.DateField(blank=True, null=True, verbose_name='Fecha de Conclusión')
    downloadedData = models.DateField(blank=True, null=True, verbose_name='Fecha Descarga Datos')

    class Meta:    
        verbose_name='Levantamiento de Campo'
        verbose_name_plural='Levantamientos de Campo'

    def __str__(self):
        return str(self.solicitud_id)


#informes
class Reports(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud')
    armedInformation = models.DateField(blank=True, null=True, verbose_name='Info. Armada')
    alignedPlan = models.DateField(blank=True, null=True, verbose_name='Plano Alineado')
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas')
    sketch = models.DateField(blank=True, null=True, verbose_name='Dibujo de Croquis')
    drafting = models.DateField(blank=True, null=True, verbose_name='Redacción del Doc.')
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
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud')
    draw = models.DateField(blank=True, null=True, verbose_name='Fecha Dibujo')
    sketch = models.DateField(blank=True, null=True, verbose_name='Laminas Terminadas')
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    submittedCurves = models.DateField(blank=True, null=True, verbose_name='Curvas entregadas el:')

    class Meta:    
        verbose_name='Curvas de Nivel'
        verbose_name_plural='Curvas de Nivel'

    def __str__(self):
        return f'Curvas de Nivel||{self.solicitud_id}'


#catastro 
class CadastralPlans(models.Model):
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud')
    draw = models.DateField(blank=True, null=True, verbose_name='Fecha Dibujo')
    review = models.DateField(blank=True, null=True, verbose_name='Revisión')
    uploadedAPT = models.DateField(blank=True, null=True, verbose_name='Subido APT')
    advertisedPlano = models.DateField(blank=True, null=True, verbose_name='Plano Catastrado el:')

    class Meta:
        verbose_name = 'Plano Catastrado'
        verbose_name_plural = 'Planos Catastrados'

    def __str__(self):
        return f'Plano Catastrado||{self.solicitud_id}'

#correciones catastro
class Corrections(models.Model):
    cadastral_id= models.ForeignKey(CadastralPlans, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Catastro')
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
    solicitud_id= models.ForeignKey(Solicitudes, on_delete=models.SET_NULL, null=True, blank=False, verbose_name='Solicitud')
    armedInformation = models.DateField(blank=True, null=True, verbose_name='Info. Armada')
    alignedPlan = models.DateField(blank=True, null=True, verbose_name='Plano Alineado') 
    replantingPoints = models.DateField(blank=True, null=True, verbose_name='Rep. Puntos en sitio')
    downloadedPhotos = models.DateField(blank=True, null=True, verbose_name='Fotos descargadas')
    sketch = models.DateField(blank=True, null=True, verbose_name='Laminas Terminadas')
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


