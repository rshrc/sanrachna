from rest_framework import serializers
from config import config
from clientele import models


class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prospect
        fields = config.PROSPECT_FIELDS


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lead
        fields = config.PROSPECT_FIELDS


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = config.PROSPECT_FIELDS
