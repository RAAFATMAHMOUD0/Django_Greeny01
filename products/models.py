from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
FLAG_TYPE = (
    ('New','New'),
    ('Feature','Feature')
)
Rate_TYPE = (
    ('1','1'),
     ('2','2'),
      ('3','3'),
       ('4','4'),
        ('5','5')
)
class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_('Sku'))
    price = models.FloatField(_("Price "))
    description = models.TextField(_("Description"), max_length=10000)
    flag = models.CharField(_("Flag"), max_length=10, choices=FLAG_TYPE)
    category = models.ForeignKey('Category',verbose_name=_('Category'),related_name='product_category',on_delete=models.SET_NULL, null=True,blank=True)
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'),related_name='product_brand',on_delete=models.SET_NULL, null=True,blank=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    photo = models.ImageField(_("Photo"), upload_to='category/')
    class Meta:
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    def __str__(self):
        return self.name
class Review(models.Model):
    product =models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_review' ,on_delete=models.SET_NULL, null=True,blank=True)
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='review_user' ,on_delete=models.SET_NULL, null=True,blank=True)
    review = models.TextField(_("Review"),max_length=1000)
    #rate = models.IntegerField(_("Rate"), validators=[MaxValueValidator(5), MinValueValidator(0)])
    rate = models.IntegerField(_("Rate"), choices=Rate_TYPE)
    created_date = models.DateTimeField(_("Created Date"), default=timezone.now)
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_image' ,on_delete=models.CASCADE)
    photo = models.ImageField(_("Photo"), upload_to='product/')
    def __str__(self):
        return str(self.product)
