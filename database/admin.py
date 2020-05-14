from django.contrib import admin
from database import models


@admin.register(models.Material)
class MaterialAdmin(admin.ModelAdmin):
    model = models.Material
    list_display = [
        'id',
        'sno',
        'particulars',
        'quantity',
        'unit',
        'rate',
        'type',
    ]


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    model = models.Service
    list_display = [
        'name',
        'unit',
        'rate',
    ]


@admin.register(models.SubService)
class SubServiceAdmin(admin.ModelAdmin):
    model = models.SubService
    list_display = [
        'service',
        'name',
    ]
