from django.db import models
from config import config


class ProspectModel(models.Model):
    full_name = models.CharField(max_length=64, default="")
    organization = models.CharField(max_length=100, default="", blank=True)
    email = models.EmailField(blank=True)
    mobile_number = models.CharField(max_length=16, default="")
    site_type = models.CharField(max_length=100, default="", choices=config.SITE_TYPES)
    source_type = models.CharField(max_length=10, default="", choices=config.SOURCE_TYPES)

    class Meta:
        abstract = True


class Prospect(ProspectModel):

    def __str__(self):
        return self.full_name
