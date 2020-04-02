from django.db import models
from prospect.models import Prospect


class Material(models.Model):
    sno = models.CharField(max_length=12, default="", blank=True)
    particulars = models.CharField(max_length=500, default="", blank=True)
    quantity = models.CharField(max_length=100, default="", blank=True)
    unit = models.CharField(max_length=100, default="", blank=True)
    rate = models.CharField(max_length=100, default="", blank=True)
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, default="")

    class Meta:
        abstract = True


class PlyMaterial(Material):

    def __str__(self):
        return self.particulars


class PaintMaterial(Material):

    def __str__(self):
        return self.particulars


class PlumbingMaterial(Material):

    def __str__(self):
        return self.particulars


class ElectricMaterial(Material):

    def __str__(self):
        return self.particulars


class TilesMaterial(Material):

    def __str__(self):
        return self.particulars


class CivilMaterial(Material):

    def __str__(self):
        return self.particulars


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
