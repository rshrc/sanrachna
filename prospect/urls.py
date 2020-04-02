from django.urls import path
from prospect import views

urlpatterns = [
    path('list/', views.ProspectListAPIView.as_view(), name='list_prospect'),
]
