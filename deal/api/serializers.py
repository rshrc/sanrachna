from rest_framework import serializers
from deal.models import Prospect, Material, Service, Associate


class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prospect
        fields = ('id', 'user', 'organization', 'email', 'site_type', 'source_type', 'status', 'complete')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'brand_name', 'material_name', 'type', 'unit', 'rate', 'description', 'prospect')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'type', 'service_name', 'description', 'rate_of_service', 'prospect')


class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associate
        fields = ('id', 'user', 'type')
