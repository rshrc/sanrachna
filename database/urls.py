from django.urls import path
from database import views

urlpatterns = [
    path('material/', views.MaterialListAPIView.as_view(), name='list_material'),
    path('material/<int:pk>/delete', views.MaterialDestroyAPIView.as_view(), name='destroy_material'),
    path('service/', views.ServiceListAPIView.as_view(), name='list_service'),
    path('service/<int:pk>/delete/', views.ServiceDestroyAPIView.as_view(), name='destroy_service')
]
