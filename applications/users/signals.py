from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from applications.users.models import User, Profile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, update, **kwargs):
    
#     if not update:
#         Profile.objects.update(
#             id=instance,
#             bio= 35
#             )

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save(bio = 4)   