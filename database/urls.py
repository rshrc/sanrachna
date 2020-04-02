from django.urls import path
from database import views

urlpatterns = [
    path('material/ply/', views.get_ply_material),
    path('material/ply/list', views.PlyMaterialListAPIView.as_view(), name='list_ply_material'),
    path('material/paint/', views.get_paint_material),
    path('material/plumbing/', views.get_plumbing_material),
    path('material/electric/', views.get_electric_material),
    path('material/tiles/', views.get_tiles_material),
    path('material/civil/', views.get_civil_material),
    path('service/', views.get_service),
    path('service/list/', views.ServiceListAPIView.as_view(), name='list_service')
]
