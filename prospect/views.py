from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from prospect import models
from prospect import serializers
from rest_framework import generics


class ProspectListAPIView(generics.ListCreateAPIView):
    queryset = models.Prospect.objects.all()
    serializer_class = serializers.ProspectSerializer
