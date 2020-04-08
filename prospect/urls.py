from django.urls import path
from prospect import views

urlpatterns = [
    path('list/', views.ProspectListAPIView.as_view(), name='list_prospect'),
    path('prospect/<int:pk>/delete/', views.ProspectDestroyAPIView.as_view(), name='destroy_prospect'),
]
