from django import forms 

class InvoiceForm(forms.Form):
    toName  = forms.CharField(label="toName",required=True)
    invoiceDate = forms.DateField(label="invoiceDate",required=True)
    ewayBill = forms.CharField(label="ewayBill",required=False)
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
    subtotal = forms.IntegerField()
    cgst = forms.FloatField()
    sgst = forms.FloatField()
    igst = forms.FloatField()
    grand = forms.FloatField()
    bankName = forms.CharField()
    accountNo = forms.CharField()
    ifscCode = forms.CharField()

    
    