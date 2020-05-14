from django.db import models
from database.models import Service, Material
from config import config


class AssociateModel(models.Model):
    full_name = models.CharField(max_length=64, default="")
    organization = models.CharField(max_length=64, default="", blank=True)
    mobile_number = models.CharField(max_length=16, default="")
    email = models.EmailField(default="")

    class Meta:
        abstract = True


class Vendor(AssociateModel):

    def __str__(self):
        return self.full_name


class Labour(AssociateModel):

    def __str__(self):
        return self.full_name


class Supervisor(AssociateModel):

    def __str__(self):
        return self.full_name


class LabourSupervisor(models.Model):
    labour = models.ForeignKey(Labour, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.labour.full_name + " " + self.supervisor.full_name


class ServiceSupervisor(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def _str__(self):
        return self.service.name + " " + self.supervisor.full_name


class MaterialVendor(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.material.particulars + " " + self.vendor.full_name
