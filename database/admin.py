from django.contrib import admin
from database import models


# @admin.register(Service)
class MaterialAdmin(admin.ModelAdmin):
    list_display = [
        'sno',
        'particulars',
        'quantity',
        'unit',
        'rate',
    ]

    class Meta:
        abstract = True


@admin.register(models.PlyMaterial)
class PlyMaterialAdmin(MaterialAdmin):
    model = models.PlyMaterial

    def __str__(self):
        pass


@admin.register(models.PaintMaterial)
class PaintMaterialAdmin(MaterialAdmin):
    model = models.PaintMaterial

    def __str__(self):
        pass


@admin.register(models.PlumbingMaterial)
class PlumbingMaterialAdmin(MaterialAdmin):
    model = models.PlumbingMaterial

    def __str__(self):
        pass


@admin.register(models.ElectricMaterial)
class ElectricMaterialAdmin(MaterialAdmin):
    model = models.ElectricMaterial

    def __str__(self):
        pass


@admin.register(models.TilesMaterial)
class TilesMaterialAdmin(MaterialAdmin):
    model = models.TilesMaterial

    def __str__(self):
        pass


@admin.register(models.CivilMaterial)
class CivilMaterialAdmin(MaterialAdmin):
    model = models.CivilMaterial

    def __str__(self):
        pass


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
