from rest_framework import serializers
from database import models as db_models
from config import config


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.Material
        fields = config.MATERIAL_FIELDS


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.Service
        fields = config.SERVICE_FIELDS
