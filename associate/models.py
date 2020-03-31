from django.db import models
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
