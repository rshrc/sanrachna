from django.db import models
from prospect.models import ProspectModel


class Prospect(ProspectModel):

    def __str__(self):
        return self.full_name


class Lead(ProspectModel):

    def __str__(self):
        return self.full_name


class Client(ProspectModel):

    def __str__(self):
        return self.full_name
