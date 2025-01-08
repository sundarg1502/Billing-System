from django.shortcuts import render, HttpResponse
from Bill.models import *
from Bill.forms import *

def invoice(request):
    company = Company.objects.all()
    # if request.method == 'POST':
    #     # c_name_req = pyth
    #     data = Company.objects.get(pk=1)
    #     # print(data.toAddress)
    #     add= data.toAddress
    #     return render(request, "invoice.html",{"company":company,"data":add})

    return render(request, "invoice.html",{"company":company})

def products(request):
    # print("Function vvallledd")
    cName = request.GET.get('toName')
    product = request.GET.get('prod')
    print(product)
    company = Company.objects.get(c_name=cName)
    print(company.c_name)
    print(company.mesh_40)

    # return HttpResponse
    # return render(request, "invoice.html",{"company":company})