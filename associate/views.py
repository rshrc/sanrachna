from associate import models
from associate import serializers
from rest_framework import generics


class VendorListAPIView(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class VendorDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer


class LabourListAPIView(generics.ListCreateAPIView):
    queryset = models.Labour.objects.all()
    serializer_class = serializers.LabourSerializer


class LabourDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Labour.objects.all()
    serializer_class = serializers.LabourSerializer


class SupervisorListAPIView(generics.ListCreateAPIView):
    queryset = models.Supervisor.objects.all()
    serializer_class = serializers.SupervisorSerializer


class SupervisorDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Supervisor.objects.all()
    serializer_class = serializers.SupervisorSerializer


class LabourMapSupervisorAPIView(generics.ListCreateAPIView):
    queryset = models.LabourSupervisor.objects.all()
    serializer_class = serializers.LabourSupervisor
