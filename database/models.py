from django.db import models


class Material(models.Model):
    class Meta:
        abstract = True


class Service(models.Model):
    name = models.CharField(max_length=64, default="")
    unit = models.CharField(max_length=12, default="")
    rate = models.CharField(max_length=16, default="")

    def __str__(self):
        return self.name


class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="")
