"""
app URL Configuration
"""
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'),
         name='api-docs'),
    path('api/user/', include('user.urls'))
]
