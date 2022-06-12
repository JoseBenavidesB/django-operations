from django.db.models.signals import post_save
from django.dispatch import receiver
from operations.models import *

""" @receiver(post_save, sender=Quotes) 
def post_save_approve_quote(sender, update_fields, instance, created, **kwargs):
    if created or not created:
        campos = kwargs.get('update_fields')
        if 'status' in campos:
            for campo in campos:
                if campo == 'Aprobada':
                    Solicitudes.objects.create(quote = instance.id, service_id = instance.service, customer_id = instance.final_customer, contact = instance.contact)

                   Preliminary.objects.create(quote = instance.id) """
@receiver(post_save, sender=Quotes)
def prueba(sender, update_fields, instance, created, **kwargs):
    if created or not created:
        if str(instance.service.typeService) != "Aprobada":
            if str(instance.status) == 'Aprobada':
                if Solicitudes.objects.filter(quote=instance).count() <= 0:
                    Solicitudes.objects.create(quote=instance)
                    Payments.objects.create(quote=instance)
                    Preliminary.objects.create(quote=instance)
                    FieldSurvey.objects.create(solicitud_id=instance)

@receiver(post_save, sender=Solicitudes) #there are two ways to use signals, the most easy is use decorator
def post_save_create_fieldsurvey(sender, instance, created, **kwargs):
    if created:

        if(str(instance.quote.service) == 'Replanteo'):
            Replant.objects.create(solicitud_id=instance.quote)
            #print('SI INCLUYE REPLANTEO ****************************************')
        elif(str(instance.quote.service) == 'Plano Catastrado'):
            CadastralPlans.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Curvas de Nivel'):
            levelCurves.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Informe'):
            Reports.objects.create(solicitud_id=instance.quote)
            print(str(instance.quote.service))
            
        elif(str(instance.quote.service) == 'Informe--Replanteo'):
            Reports.objects.create(solicitud_id=instance.quote)
            Replant.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Informe--Curvas de Nivel'):
            Reports.objects.create(solicitud_id=instance.quote)
            levelCurves.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Curvas de Nivel--Replanteo'):
            Replant.objects.create(solicitud_id=instance.quote)
            levelCurves.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Informe--Catastro'):
            Reports.objects.create(solicitud_id=instance.quote)
            CadastralPlans.objects.create(solicitud_id=instance.quote)
            
        elif(str(instance.quote.service) == 'Informe--Catastro--Curvas de Nivel'):
            Reports.objects.create(solicitud_id=instance.quote)
            CadastralPlans.objects.create(solicitud_id=instance.quote)
            levelCurves.objects.create(solicitud_id=instance.quote)
        
        elif(str(instance.quote.service) == 'Informe--Replanteo--Curvas de Nivel'):
            Reports.objects.create(solicitud_id=instance.quote)
            Replant.objects.create(solicitud_id=instance.quote)
            levelCurves.objects.create(solicitud_id=instance.quote)
            

