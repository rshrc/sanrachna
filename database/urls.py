from django.urls import path
from database import views

urlpatterns = [
    path('material/ply/', views.PlyMaterialListAPIView.as_view(), name='list_ply_material'),
    path('material/paint/', views.PaintMaterialListAPIView.as_view(), name='list_paint_material'),
    path('material/plumbing/', views.PlumbingMaterialListAPIView.as_view(), name='list_plumbing_material'),
    path('material/electric/', views.ElectricMaterialListAPIView.as_view(), name='list_electric_material'),
    path('material/tiles/', views.TilesMaterialListAPIView.as_view(), name='list_tiles_material'),
    path('material/civil/', views.CivilMaterialListAPIView.as_view(), name='list_civil_material'),
    path('service/', views.get_service),
    path('service/list/', views.ServiceListAPIView.as_view(), name='list_service')
]
