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
        if filledform.is_valid():
            filled_data = {key: value for key, value in filledform.cleaned_data.items() if value}
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
    return JsonResponse({'price':rate})

def generatebill(datas):
    invoice_details = {
        'invoice_no': 'INV-001',
        'date': '11-01-2025',
        'gstin': '29ABCDE1234F1Z5',
        'shipping_address': '123 Main St, Bangalore - 560001',
        'eway_bill': 'EWB12345'
    }
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

    doc = Document("static/Template.docx")
    table = doc.tables[0]  
    date = datas["invoiceDate"].strftime("%d-%m-%Y")
    
    # table.rows[1].cells[3].text = f"To : {datas.get('toName', '')},{datas.get('shippingAddress', '')}"
    to_bold = table.rows[1].cells[3]
    to_cell = to_bold.paragraphs[0].clear()
    to_cell.add_run("To :").bold=True
    to_cell.add_run(f"{datas.get('toName', '')},{datas.get('shippingAddress', '')}")

    table.rows[1].cells[7].text = "1234"
    table.rows[2].cells[7].text = date
    gst_bold = table.rows[3].cells[0]
    gst_cell = gst_bold.paragraphs[0].clear()
    gst_cell.add_run("PARTY'S GSTIN NO:").bold=True
    gst_cell.add_run(datas.get('gstin', ''))
    
    if invoice_details.get('eway_bill'):
        table.rows[3].cells[7].text = invoice_details['eway_bill']
    
    table.rows[4].cells[4].text = f"Shipping address : "

    total_amount = 0
    for idx, (desc, hsn, qty, rate) in enumerate(items, 1):
        row = table.rows[idx + 5]  
        amount = float(qty) * float(rate)
        total_amount += amount
        row.cells[0].text = str(idx)
        row.cells[1].text = desc+" Titanium Powder"
        row.cells[5].text = str(hsn)
        row.cells[6].text = str(qty)+" KG"
        row.cells[8].text = str(rate)
        row.cells[9].text = f"{amount:.2f}"
    
    table.rows[10].cells[9].text = f"{total_amount:.2f}"  
    
    cgst = total_amount * 0.09
    sgst = total_amount * 0.09
    # igst = total_amount * 0.18
    
    table.rows[11].cells[9].text = f"{cgst:.2f}"  
    table.rows[12].cells[9].text = f"{sgst:.2f}"   
    
    total_after_tax = total_amount + cgst + sgst
    table.rows[14].cells[9].text = f"{total_after_tax:.2f}"
    
    p = inflect.engine()
    table.rows[15].cells[2].text =  p.number_to_words(total_after_tax) +" rupees only"

    doc.save(f"static/invoices/{datas.get('toName', '')}_INV_{randint(1,100)}.docx")