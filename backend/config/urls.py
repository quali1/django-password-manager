from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manager.views import PSManagerViewSet

router = routers.SimpleRouter()
router.register(r'psm', PSManagerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include(router.urls))
]
