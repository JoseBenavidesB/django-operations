from django.db.models.signals import post_save
from django.dispatch import receiver
from operations.models import Solicitudes, FieldSurvey, Reports, levelCurves, CadastralPlans, Replant


@receiver(post_save, sender=Solicitudes) #there are two ways to use signals, the most easy is use decorator
def post_save_create_fieldsurvey(sender, instance, created, **kwargs):
    if created:
        if instance.survey:
            FieldSurvey.objects.create(solicitud_id = instance)

        if(str(instance.service_id) == 'Replanteo'):
            Replant.objects.create(solicitud_id=instance)
        elif(str(instance.service_id) == 'Plano Catastrado'):
            CadastralPlans.objects.create(solicitud_id=instance)
        elif(str(instance.service_id) == 'Curvas de Nivel'):
            levelCurves.objects.create(solicitud_id=instance)
        elif(str(instance.service_id) == 'Informe'):
            Reports.objects.create(solicitud_id=instance)

