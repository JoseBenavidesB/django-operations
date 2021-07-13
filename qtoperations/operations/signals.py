from django.db.models.signals import post_save
from django.dispatch import receiver
from operations.models import Solicitudes, FieldSurvey, Reports, levelCurves, CadastralPlans, Replant


@receiver(post_save, sender=Solicitudes) #there is two ways to use signals, the most easy is use decorator
def post_save_create_fieldsurvey(sender, instance, created, **kwargs):
    if created:
        FieldSurvey.objects.create(request=instance)

@receiver(post_save, sender=FieldSurvey)
def post_save_create_job(sender, instance, created, **kwargs):
    if created:
        if(str(instance.request.service) == 'Replanteo'):
            Replant.objects.create(request=instance)
        elif(str(instance.request.service) == 'Plano Catastrado'):
            CadastralPlans.objects.create(request=instance)
        elif(str(instance.request.service) == 'Curvas de Nivel'):
            levelCurves.objects.create(request=instance)
        else:
            Reports.objects.create(request=instance)