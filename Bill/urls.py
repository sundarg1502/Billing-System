from django.urls import path
from Bill import views

app_name = 'Bill'

urlpatterns = [
    path('', views.invoice, name='invoice'),
    path('products/', views.products, name='products'),
    path('address/', views.address, name='address'),
]