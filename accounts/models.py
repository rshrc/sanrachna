from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=40, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=17, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    display_image = models.ImageField(upload_to='media/', default='', blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.email
