from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def get_prospect(request, prospect_id):
    pass


@api_view(['GET'])
def get_prospects(request):
    pass


@api_view(['GET'])
def get_materials(request, prospect_id):
    pass


@api_view(['GET'])
def get_services(request, prospect_id):
    pass


@api_view(['GET'])
def get_associates(request):
    pass


@api_view(['POST'])
def create_prospect(request):
    pass


@api_view(['POST'])
def create_material(request):
    pass


@api_view(['POST'])
def create_service(request):
    pass


@api_view(['POST'])
def create_associate(request):
    pass


class ProspectUpdateView(generics.UpdateAPIView):
    pass


class MaterialUpdateView(generics.UpdateAPIView):
    pass


class ServiceUpdateView(generics.UpdateAPIView):
    pass


class AssociateUpdateView(generics.UpdateAPIView):
    pass
