from rest_framework import viewsets
from .models import Hazard
from .serializers import HazardSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HazardViewSet(viewsets.ModelViewSet):
    queryset = Hazard.objects.all()
    serializer_class = HazardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]