from django.shortcuts import render
from django.http import JsonResponse
from Bill.models import *
from Bill.forms import *
from Bill.forms import *
from docx import Document
from datetime import datetime
from random import randint
import inflect

def invoice(request):
    company = Company.objects.all()
    if request.method == 'POST':
        filledform = InvoiceForm(request.POST)
        print(filledform.is_valid())
        for error in filledform.errors:
            print(error)
            
        if filledform.is_valid():
            # to = filledform.cleaned_data['toName']
            # date = filledform.cleaned_data['invoiceDate']
            # shippingAddress = filledform.cleaned_data['shippingAddress']
            # product1 = filledform.cleaned_data['product1']
            # qty1 = filledform.cleaned_data['qty1']
            # rate1 = filledform.cleaned_data['rate1']
            # amt1 = filledform.cleaned_data['amount1']
            # to = filledform.cleaned_data['product2']
            filled_data = {key: value for key, value in filledform.cleaned_data.items() if value}
            # print(filled_data)
            generatebill(filled_data)
    return render(request, "invoice.html",{"company":company})

def address(request):
    add = Company.objects.get(c_name=request.GET.get('toName')).toAddress
    gst = Company.objects.get(c_name=request.GET.get('toName')).gstIN
    return JsonResponse({'add':add,'gst':gst})

def products(request):
    cName = request.GET.get('toName')
    product = request.GET.get('prod')
    print(product)
    company = Company.objects.get(c_name=cName)
    rate = getattr(company,product)
    # toName = company.toAddress
    
    return JsonResponse({'price':rate})

def generatebill(datas):
    print(datas)
    # Invoice details
    invoice_details = {
        'invoice_no': 'INV-001',
        'date': '11-01-2025',
        'gstin': '29ABCDE1234F1Z5',
        'shipping_address': '123 Main St, Bangalore - 560001',
        'eway_bill': 'EWB12345'
    }
    
    # List of items (description, HSN, quantity, rate)
    items = [
    ]
    try:
        for i in range(1,5):
            print(i)
            if datas[f"product{i}"]:
                product_name = datas[f"product{i}"]
                qty = datas[f"qty{i}"]
                rate = datas[f"rate{i}"]
                product = (product_name,"81082000",qty,rate)
                items.append(product)
    except:
        pass

    print(items)
    # Load the document
    doc = Document("static/Template.docx")
    table = doc.tables[0]  # Get the main table
    date = datas["invoiceDate"].strftime("%d-%m-%Y")
    # Update header information
    table.rows[1].cells[3].text = f"To : {datas.get('toName', '')}"
    table.rows[1].cells[7].text = "1234"
    table.rows[2].cells[7].text = date
    table.rows[3].cells[0].text = f"PARTY'S GSTIN NO: {datas.get('gstin', '')}"
    
    if invoice_details.get('eway_bill'):
        table.rows[3].cells[7].text = invoice_details['eway_bill']
    
    table.rows[4].cells[4].text = f"Shipping address : {datas.get('shippingAddress', '')}"
    
    # Update items and calculate total
    total_amount = 0
    for idx, (desc, hsn, qty, rate) in enumerate(items, 1):
        row = table.rows[idx + 5]  # Items start from row 6
        amount = float(qty) * float(rate)
        total_amount += amount
        
        # Fill item details
        row.cells[0].text = str(idx)
        row.cells[1].text = desc+" Titanium Powder"
        row.cells[5].text = str(hsn)
        row.cells[6].text = str(qty)+" KG"
        row.cells[8].text = str(rate)
        row.cells[9].text = f"{amount:.2f}"
    
    # Update totals and taxes
    table.rows[10].cells[9].text = f"{total_amount:.2f}"  # Total before tax
    
    # Calculate taxes
    cgst = total_amount * 0.09
    sgst = total_amount * 0.09
    igst = total_amount * 0.18
    
    # Update tax amounts
    table.rows[11].cells[9].text = f"{cgst:.2f}"  # CGST
    table.rows[12].cells[9].text = f"{sgst:.2f}"  # SGST
    table.rows[13].cells[9].text = f"{igst:.2f}"  # IGST
    
    # Total after tax (using CGST + SGST)
    total_after_tax = total_amount + cgst + sgst
    table.rows[14].cells[9].text = f"{total_after_tax:.2f}"
    
    p = inflect.engine()
    table.rows[15].cells[2].text =  p.number_to_words(total_after_tax) +" rupees only"

    # Save the document
    doc.save(f"static/invoices/b{randint(1,1000)}.docx")