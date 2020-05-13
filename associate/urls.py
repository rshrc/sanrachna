from django.urls import path
from associate import views

urlpatterns = [
    path('vendor/', views.VendorListAPIView.as_view(), name='list_vendor'),
    path('vendor/<int:pk>/delete/', views.VendorDestroyAPIView.as_view(), name='destroy_vendor'),
    path('labour/', views.LabourListAPIView.as_view(), name='list_labour'),
    path('labour/<int:pk>/delete/', views.LabourDestroyAPIView.as_view(), name='destroy_labour'),
    path('supervisor/', views.SupervisorListAPIView.as_view(), name='list_supervisor'),
    path('supervisor/<int:pk>/delete/', views.SupervisorDestroyAPIView.as_view(), name='destroy_supervisor'),
    path('mls/', views.LabourMapSupervisorAPIView.as_view(), name='mls'),
    path('mss/', views.ServiceMapSupervisorAPIView.as_view(), name='mss'),
    path('mmv/', views.MaterialMapVendorAPIView.as_view(), name='mmv'),

]
