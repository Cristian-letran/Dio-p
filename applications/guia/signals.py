# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from applications.guia.models import img, Guia

# @receiver(post_save, sender=Guia)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         img.objects.create(id_guia=instance)   

# from applications.datos_g.models import datos_g
# from applications.guia.models import Guia
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.conf import settings

# @receiver(post_save, sender=Guia)
# def create_user_rastreo(sender, instance, created, **kwargs):
#     instance.datos_g.save()   
    # if not created:
    #     # datos_g.objects.create(    
    #     return
    # datos_g.objects.create(seudo_dg= instance)
            
           
            