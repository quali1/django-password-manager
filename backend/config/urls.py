from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manager.views import PSManagerViewSet

router = routers.DefaultRouter()
router.register(r'saved-passwords', PSManagerViewSet, basename='saved-passwords')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include(router.urls)),
]
