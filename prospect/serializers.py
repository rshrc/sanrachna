from rest_framework import serializers
from prospect import models
from config import config


class ProspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prospect
        fields = config.PROSPECT_FIELDS
