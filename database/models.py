from django.db import models
from prospect.models import Prospect
from config import config


class Material(models.Model):
    sno = models.CharField(max_length=12, default="", blank=True)
    particulars = models.CharField(max_length=500, default="", blank=True)
    quantity = models.CharField(max_length=100, default="", blank=True)
    unit = models.CharField(max_length=100, default="", blank=True)
    rate = models.CharField(max_length=100, default="", blank=True)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, default="")
    type = models.CharField(max_length=12, default="", choices=config.MATERIAL_TYPES)
    remark = models.CharField(max_length=140, default="", blank=True)

    def __str__(self):
        return self.particulars + " " + self.type


class Service(models.Model):
    name = models.CharField(max_length=64, default="")
    unit = models.CharField(max_length=12, default="")
    rate = models.CharField(max_length=16, default="")
    prospect = models.ForeignKey(Prospect, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="")
