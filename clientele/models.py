from django.db import models


class ClienteleModel(models.Model):
    class Meta:
        abstract = True


class Prospect(ClienteleModel):
    pass


class Lead(ClienteleModel):
    pass


class Client(ClienteleModel):
    pass
