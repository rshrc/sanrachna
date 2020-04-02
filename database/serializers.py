from rest_framework import serializers
from database import models as db_models
from config import config


class PlyMaterialSerializer(serializers.ModelSerializer):
    # prospect_name = serializers.RelatedField(source='prospect', read_only=True)

    class Meta:
        model = db_models.PlyMaterial
        fields = config.MATERIAL_FIELDS


class PaintMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.PaintMaterial
        fields = config.MATERIAL_FIELDS


class PlumbingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.PlumbingMaterial
        fields = config.MATERIAL_FIELDS


class ElectricMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.ElectricMaterial
        fields = config.MATERIAL_FIELDS


class TilesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.TilesMaterial
        fields = config.MATERIAL_FIELDS


class CivilMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.CivilMaterial
        fields = config.MATERIAL_FIELDS


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = db_models.Service
        fields = config.SERVICE_FIELDS