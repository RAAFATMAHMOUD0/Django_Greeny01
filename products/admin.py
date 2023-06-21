from django.contrib import admin
from .models import *

# Register your models here.
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Brand)