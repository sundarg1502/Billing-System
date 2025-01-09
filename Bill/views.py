from django.shortcuts import render
from django.http import JsonResponse
from Bill.models import *
from Bill.forms import *

def invoice(request):
    company = Company.objects.all()
    return render(request, "invoice.html",{"company":company})

def address(request):
    add = Company.objects.get(c_name=request.GET.get('toName')).toAddress
    return JsonResponse({'add':add})

def products(request):
    cName = request.GET.get('toName')
    product = request.GET.get('prod')
    print(product)
    company = Company.objects.get(c_name=cName)
    rate = getattr(company,product)
    # toName = company.toAddress
    
    return JsonResponse({'price':rate})