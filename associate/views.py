from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from associate import models
from associate import serializers
from rest_framework import generics


class VendorListAPIView(generics.ListCreateAPIView):
    queryset = models.Vendor
    serializer_class = serializers.VendorSerializer


class LabourListAPIView(generics.ListCreateAPIView):
    queryset = models.Labour
    serializer_class = serializers.LabourSerializer


class SupervisorListAPIView(generics.ListCreateAPIView):
    queryset = models.Supervisor
    serializer_class = serializers.SupervisorSerializer
