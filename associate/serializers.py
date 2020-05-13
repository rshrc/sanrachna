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


"""
Serializer for mapping Labour to Supervisor
"""


class LabourSupervisor(serializers.ModelSerializer):
    supervisor_name = serializers.CharField(read_only=True, source='supervisor.full_name')
    labour_name = serializers.CharField(read_only=True, source='labour.full_name')

    class Meta:
        model = models.LabourSupervisor
        fields = ('supervisor_name', 'labour_name')


class LabourSupervisorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LabourSupervisor
        fields = ('labour', 'supervisor')


class ServiceSupervisor(serializers.ModelSerializer):
    service_name = serializers.CharField(read_only=True, source='service.name')
    supervisor_name = serializers.CharField(read_only=True, source='supervisor.full_name')

    class Meta:
        model = models.ServiceSupervisor
        fields = ('supervisor_name', 'service_name')


class ServiceSupervisorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceSupervisor
        fields = ('supervisor', 'service')


class MaterialVendor(serializers.ModelSerializer):
    material_name = serializers.CharField(read_only=True, source='material.particulars')
    vendor_name = serializers.CharField(read_only=True, source='vendor.full_name')

    class Meta:
        model = models.MaterialVendor
        fields = ('material_name', 'vendor_name')


class MaterialVendorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaterialVendor
        fields = ('material', 'vendor')
