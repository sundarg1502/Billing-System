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

    def __str__(self):
        return self.c_name


class Bill(models.Model):
    bno = models.IntegerField() 
    toName = models.CharField(max_length=150)
    gstin = models.CharField(max_length=25)
    invoiceDate = models.DateField()
    eWayBill = models.CharField(max_length=15)
    toAdd = models.CharField(max_length=150)
    shippingAdd = models.CharField(max_length=150,null=True)
    # qty = models.IntegerField()
    # amount = models.IntegerField()  
    bankName = models.CharField(max_length=15)
    accNo = models.CharField(max_length=12)  
    ifscCode = models.CharField(max_length=12)  

    def __str__(self):
        return f"{self.bno}--{self.toName}"

class Products(models.Model):
    bill = models.ForeignKey(Bill,on_delete=models.CASCADE)
    items = models.CharField(max_length=50)
    hsn = models.CharField(max_length=45)
    qty = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    amt = models.CharField(max_length=50)
    grandTotal = models.IntegerField()
