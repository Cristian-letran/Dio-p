from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class BdManager(models.Manager):
    def buscar_bd(self, kword, order):
        consulta = self.filter(
            Q(seudo_bd__icontains=kword) | Q(seudo_bd__icontains=kword)
        )

        return consulta
            