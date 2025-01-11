from django.db import models

# Create your models here.
class Company(models.Model):

    c_name = models.CharField(max_length=50)
    gstIN = models.CharField(max_length=20)
    toAddress = models.TextField()
    mesh_30 = models.IntegerField() 
    mesh_40 = models.IntegerField() 
    mesh_60 = models.IntegerField() 
    mesh_80 = models.IntegerField() 
    mesh_150 = models.IntegerField() 
    mesh_30_40 = models.IntegerField() 
    mesh_40_60 = models.IntegerField() 
    mesh_60_80 = models.IntegerField() 
    mesh_80_100 = models.IntegerField() 

class Bill(models.Model):
    toName = models.CharField(max_length=50)
    invoiceDate = models.DateTimeField()
    eWayBill = models.CharField(max_length=15)
    shippingAddress = models.TextField()
    