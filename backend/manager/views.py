from rest_framework import viewsets
from .models import SavedPassword
from .serializers import PSManagerSerializer
from .services import api_encrypt_password


# Create your views here.


class PSManagerViewSet(viewsets.ModelViewSet):
    """
    get -> list -> Retrieves a queryset of Saved Password instances.
    get -> retrieve -> Retrieves a single Saved Password instance detail view.
    post -> create -> Save a Saved Password instance.
    put -> update -> Updates an existing Saved Password instance.
    patch -> partial_update -> Partially updates an existing HydroponicSystem instance.
    delete -> destroy -> Deletes a HydroponicSystem instance.
    """
    serializer_class = PSManagerSerializer
    queryset = SavedPassword.objects.all()

    def get_queryset(self):
        return SavedPassword.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer = api_encrypt_password(serializer, self.request.user)
        serializer.save()

    def perform_update(self, serializer):
        serializer = api_encrypt_password(serializer, self.request.user)
        serializer.save()
