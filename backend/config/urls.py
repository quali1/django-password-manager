from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manager.views import PSManagerViewSet
from users.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'saved-passwords', PSManagerViewSet, basename='saved-passwords')
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include(router.urls)),
]
