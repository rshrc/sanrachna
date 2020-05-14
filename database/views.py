from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from database import models
from database import serializers
from rest_framework import generics


class MaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class MaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer


class ServiceListAPIView(generics.ListCreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


@api_view(['GET'])
def get_service(request):
    try:
        services = models.Service.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)
