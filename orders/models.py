from django.db import models
from django.utils import timezone
import random
from django.utils.translation import gettext as _
from products.models import Product

# Create your models here.
def generaste_code(length=8):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range (length))

STUTS_CHOICES = (
    ('Recieved','Recieved'),
    ('Processod','Processod'),
    ('Shipped','Shipped'),
    ('Deliverod','Recieved'),
)
class Order(models.Model):
    code = models.CharField(_("Code"), max_length=8, default=generaste_code)
    order_stuts = models.CharField(_("Order Stuts"), max_length=50, choices=STUTS_CHOICES)
    order_time = models.DateTimeField(_("Order Time"), default=timezone.now)
    deliver_time = models.DateTimeField(_("Deliver Time"), null=True, blank=True)

    def __str__(self):
        return self.code



class OrderDateil(models.Model):
    order= models.ForeignKey(Order, verbose_name=_("Order Dateil"),related_name='order_dateil',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='order_product',on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField(_("Price"))
    quantite = models.FloatField(_("Quantite"))


    def __str__(self):
        return str(self.order)