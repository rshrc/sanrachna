from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/database/', include('database.urls')),
    path('api/prospect/', include('prospect.urls')),
    path('api/clientele/', include('clientele.urls')),
]
