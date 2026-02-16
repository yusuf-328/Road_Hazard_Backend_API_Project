from rest_framework import viewsets, generics
from .models import Hazard
from .serializers import HazardSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsReporterOrAdmin

class HazardViewSet(viewsets.ModelViewSet):
    queryset = Hazard.objects.all()
    serializer_class = HazardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsReporterOrAdmin]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)
