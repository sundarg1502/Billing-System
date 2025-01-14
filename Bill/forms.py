from django import forms 
from Bill.models import *
class InvoiceForm(forms.ModelForm):
    dbupdate = forms.CharField()
    bno = forms.IntegerField()
    toName  = forms.CharField(label="toName",required=True)
    invoiceDate = forms.DateField(label="invoiceDate",required=True)
    eWayBill = forms.CharField(label="ewayBill",required=False)
    gstin = forms.CharField(required=False)
    shippingAddress = forms.CharField(label="shippingAddress")
    product1 = forms.CharField(label="product1",required=True)
    qty1 = forms.IntegerField()
    rate1 = forms.IntegerField()
    amount1 = forms.IntegerField()
    product2 = forms.CharField(label="product2",required=False, )
    qty2 = forms.IntegerField(required=False, )
    rate2 = forms.IntegerField(required=False, )
    amount2 = forms.IntegerField(required=False, )
    product3 = forms.CharField(required=False, )
    qty3 = forms.IntegerField(required=False, )
    rate3 = forms.IntegerField(required=False, )
    amount3 = forms.IntegerField(required=False, )
    product4 = forms.CharField(required=False, )
    qty4 = forms.IntegerField(required=False, )
    rate4 = forms.IntegerField(required=False, )
    amount4 = forms.IntegerField(required=False, )
    # subtotal = forms.IntegerField()
    # cgst = forms.FloatField()
    # sgst = forms.FloatField()
    # igst = forms.FloatField()
    # grand = forms.FloatField()
    bankName = forms.CharField()
    accNo = forms.CharField()
    ifscCode = forms.CharField()
    
    # def clean(self):
    #     filledform = super().clean()
    #     filled_data = {key: value for key, value in filledform.cleaned_data.items() if value}
    
    class Meta: 
        model = Bill
        fields = ['bno','toName',"gstin","invoiceDate","shippingAddress","eWayBill",
                  # "product",
                #   "qty","amt1",
                  "bankName","accNo","ifscCode"]



    