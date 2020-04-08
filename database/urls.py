from django.urls import path
from database import views

urlpatterns = [
    path('material/ply/', views.PlyMaterialListAPIView.as_view(), name='list_ply_material'),
    path('material/ply/<int:pk>/delete/', views.PlyMaterialDestroyAPIView.as_view(), name='destroy_ply_material'),
    path('material/paint/', views.PaintMaterialListAPIView.as_view(), name='list_paint_material'),
    path('material/paint/<int:pk>/delete/', views.PaintMaterialDestroyAPIView.as_view(), name='destroy_paint_material'),
    path('material/plumbing/', views.PlumbingMaterialListAPIView.as_view(), name='list_plumbing_material'),
    path('material/plumbing/<int:pk>/delete/', views.PlumbingMaterialDestroyAPIView.as_view(),
         name='destroy_plumbing_material'),
    path('material/electric/', views.ElectricMaterialListAPIView.as_view(), name='list_electric_material'),
    path('material/electric/<int:pk>/delete/', views.ElectricMaterialDestroyAPIView.as_view(),
         name='destroy_electric_material'),
    path('material/tiles/', views.TilesMaterialListAPIView.as_view(), name='list_tiles_material'),
    path('material/tiles/<int:pk>/delete/', views.TilesMaterialDestroyAPIView.as_view(), name='destroy_tiles_material'),
    path('material/civil/', views.CivilMaterialListAPIView.as_view(), name='list_civil_material'),
    path('material/civil/<int:pk>/delete/', views.CivilMaterialDestroyAPIView.as_view(), name='destroy_civil_material'),
    path('service/', views.ServiceListAPIView.as_view(), name='list_service'),
    path('service/<int:pk>/delete/', views.ServiceDestroyAPIView.as_view(), name='list_service')
]
