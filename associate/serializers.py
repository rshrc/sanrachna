from rest_framework import serializers
from associate import models
from config import config


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = config.ASSOCIATE_FIELDS


class LabourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Labour
        fields = config.ASSOCIATE_FIELDS


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supervisor
        fields = config.ASSOCIATE_FIELDS
