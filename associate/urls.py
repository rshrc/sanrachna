from django.urls import path
from associate import views

urlpatterns = [
    path('vendor/', views.VendorListAPIView.as_view(), name='list_vendor'),
    path('labour/', views.LabourListAPIView.as_view(), name='list_labour'),
    path('supervisor/', views.SupervisorListAPIView.as_view(), name='list_supervisor'),
]
