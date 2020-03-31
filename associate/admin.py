from django.contrib import admin
from associate import models


class AssociateAdmin(admin.ModelAdmin):
    list_display = [
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
