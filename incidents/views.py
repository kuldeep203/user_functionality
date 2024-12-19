from rest_framework import viewsets, permissions
from .models import Incident
from .serializers import IncidentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Limit the incidents to only those created by the logged-in user.
        """
        return Incident.objects.filter(reporter=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the reporter to the logged-in user.
        """
        serializer.save(reporter=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        Prevent updates on incidents that are closed.
        """
        incident = self.get_object()
        if incident.status == 'Closed':
            return Response({"detail": "Closed incidents cannot be edited."}, status=400)

        return super().update(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Ensure users can only view their own incidents.
        """
        incident = self.get_object()
        if incident.reporter != request.user:
            return Response({"detail": "You do not have permission to view this incident."}, status=403)
        return super().retrieve(request, *args, **kwargs)
