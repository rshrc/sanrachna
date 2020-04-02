from django.urls import path
from clientele import views

urlpatterns = [
    path('prospect/', views.ProspectListAPIView.as_view(), name='list_prospect'),
    path('lead/', views.LeadListAPIView.as_view(), name='list_lead'),
    path('client/', views.ClientListAPIView.as_view(), name='list_client'),
]
