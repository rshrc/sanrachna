from rest_framework import generics
from clientele import models
from clientele import serializers


class ProspectListAPIView(generics.ListCreateAPIView):
    queryset = models.Prospect.objects.all()
    serializer_class = serializers.ProspectSerializer


class ProspectDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Prospect.objects.all()
    serializer_class = serializers.ProspectSerializer


class LeadListAPIView(generics.ListCreateAPIView):
    queryset = models.Lead.objects.all()
    serializer_class = serializers.LeadSerializer


class LeadDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Lead.objects.all()
    serializer_class = serializers.ProspectSerializer


class ClientListAPIView(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ClientDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ProspectSerializer
