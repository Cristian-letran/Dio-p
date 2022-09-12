from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class CourrierManager(models.Manager):
    def buscar_producto(self, kword, order):
        consulta = self.filter(
            Q(courrier__icontains=kword) | Q(d_i__icontains=kword) | Q(id_ciu__ciudad__icontains=kword)
        )

        return consulta