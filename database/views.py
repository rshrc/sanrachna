from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from database import models
from database import serializers
from rest_framework import generics
from braces.views import CsrfExemptMixin
from django.views.decorators.csrf import csrf_exempt


# even takes post request
class PlyMaterialListAPIView(CsrfExemptMixin, generics.ListCreateAPIView):
    authentication_classes = []
    queryset = models.PlyMaterial.objects.all()
    serializer_class = serializers.PlyMaterialSerializer


class PlyMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.PlyMaterial.objects.all()
    serializer_class = serializers.PlyMaterialSerializer


class PaintMaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.PaintMaterial.objects.all()
    serializer_class = serializers.PaintMaterialSerializer


class PaintMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.PaintMaterial.objects.all()
    serializer_class = serializers.PaintMaterialSerializer


class PlumbingMaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.PlumbingMaterial.objects.all()
    serializer_class = serializers.PlumbingMaterialSerializer


class PlumbingMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.PlumbingMaterial.objects.all()
    serializer_class = serializers.PlumbingMaterialSerializer


class ElectricMaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.ElectricMaterial.objects.all()
    serializer_class = serializers.ElectricMaterialSerializer


class ElectricMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.ElectricMaterial.objects.all()
    serializer_class = serializers.ElectricMaterialSerializer


class TilesMaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.TilesMaterial.objects.all()
    serializer_class = serializers.TilesMaterialSerializer


class TilesMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.TilesMaterial.objects.all()
    serializer_class = serializers.TilesMaterialSerializer


class CivilMaterialListAPIView(generics.ListCreateAPIView):
    queryset = models.CivilMaterial.objects.all()
    serializer_class = serializers.CivilMaterialSerializer


class CivilMaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = models.CivilMaterial.objects.all()
    serializer_class = serializers.CivilMaterialSerializer


class ServiceListAPIView(generics.ListCreateAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class ServiceDestroyAPIView(generics.DestroyAPIView):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer


@api_view(['GET'])
def get_ply_material(request):
    try:
        materials = models.PlyMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PlyMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_paint_material(request):
    try:
        materials = models.PaintMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PaintMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_plumbing_material(request):
    try:
        materials = models.PlumbingMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.PlumbingMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_electric_material(request):
    try:
        materials = models.ElectricMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ElectricMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_tiles_material(request):
    try:
        materials = models.TilesMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.TilesMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_civil_material(request):
    try:
        materials = models.CivilMaterial.objects.all()
        print(materials)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.CivilMaterialSerializer(materials, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_service(request):
    try:
        services = models.Service.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.ServiceSerializer(services, many=True)
        return Response(serializer.data)
