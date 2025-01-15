from django.contrib import admin

# Register your models here.
from Bill.models import *

admin.site.register(Bill)
admin.site.register(Company)
admin.site.register(Products)