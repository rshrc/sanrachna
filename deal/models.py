from django.db import models

from config import config
from accounts.models import Profile


class Prospect(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    organization = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    site_type = models.CharField(max_length=20, choices=config.SITE_TYPES)
    source_type = models.CharField(max_length=20, choices=config.SOURCE_TYPES)
    status = models.CharField(max_length=20, choices=config.PROSPECT_TYPES, blank=True)
    complete = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return "Prospect for {}".format(self.user.email)


# Brand Name, Material Name, Type, Unit, Rate, Description.
class Material(models.Model):
    brand_name = models.CharField(max_length=100)
    material_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=config.MATERIAL_TYPES)
    unit = models.CharField(max_length=100)
    rate = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    prospect = models.ForeignKey(to=Prospect, related_name='materials', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.brand_name + " " + self.material_name


# Service Type, Service Name, Description, Rate of service (unit-wise)
class Service(models.Model):
    type = models.CharField(max_length=100, choices=config.SERVICE_TYPES)
    service_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rate_of_service = models.CharField(max_length=20)
    prospect = models.ForeignKey(to=Prospect, related_name='services', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.service_name + self.type


class Associate(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default="")
    type = models.CharField(max_length=20, choices=config.ASSOCIATE_TYPES)

    def __str__(self):
        return self.user.email + " " + self.type
