from django.contrib import admin
from associate import models


class AssociateAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'organization',
        'mobile_number',
        'email',
    ]

    class Meta:
        abstract = True


@admin.register(models.Vendor)
class VendorAdmin(AssociateAdmin):
    model = models.Vendor

    def __str__(self):
        pass


@admin.register(models.Labour)
class LabourAdmin(AssociateAdmin):
    model = models.Labour

    def __str__(self):
        pass


@admin.register(models.Supervisor)
class SupervisorAdmin(AssociateAdmin):
    model = models.Supervisor

    def __str__(self):
        pass


@admin.register(models.LabourSupervisor)
class LabourSupervisor(admin.ModelAdmin):
    model = models.LabourSupervisor

    list_display = [
        'labour',
        'supervisor',
    ]


@admin.register(models.ServiceSupervisor)
class ServiceSupervisor(admin.ModelAdmin):
    model = models.ServiceSupervisor

    list_display = [
        'service',
        'supervisor',
    ]


@admin.register(models.MaterialVendor)
class MaterialVendor(admin.ModelAdmin):
    model = models.MaterialVendor

    list_display = [
        'material',
        'vendor',
    ]
