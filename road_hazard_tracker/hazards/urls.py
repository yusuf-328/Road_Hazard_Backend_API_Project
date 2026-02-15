from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HazardViewSet

router = DefaultRouter()
router.register(r'hazards', HazardViewSet, basename='hazard')

urlpatterns = [
    path('api/', include(router.urls)),
]