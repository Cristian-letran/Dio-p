from .managers import ProductManagers
from django.db import models
from django.db.models import Q, F

class ProductManager(models.Manager):
    """ procedimiento modelo product """

    def buscar_producto(self, kword, order):
        consulta = self.filter(
            Q(name__icontains=kword) | Q(barcode=kword)
        )