from django.urls import path
from .views import ProductList,ProductDateil

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>', ProductDateil.as_view(), name='product_dateil'),
]
