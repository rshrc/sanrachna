from django.urls import path
from clientele import views

urlpatterns = [
    path('prospect/', views.ProspectListAPIView.as_view(), name='list_prospect'),
    path('prospect/<int:pk>/delete/', views.ProspectDestroyAPIView.as_view(), name='destroy_prospect'),
    path('lead/', views.LeadListAPIView.as_view(), name='list_lead'),
    path('lead/<int:pk>/delete/', views.LeadDestroyAPIView.as_view(), name='destroy_lead'),
    path('client/', views.ClientListAPIView.as_view(), name='list_client'),
    path('client/<int:pk>/delete/', views.ClientDestroyAPIView.as_view(), name='destroy_client'),

]
