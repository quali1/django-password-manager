from rest_framework import viewsets
from .models import SavedPassword
from .serializers import PSManagerSerializer
from .encryption import PasswordManagerEncryption
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

    def perform_create(self, serializer):
        pme = PasswordManagerEncryption()
        password = serializer.validated_data['password']
        password, key = pme.encrypt_password(password)

        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['password'] = password
        serializer.validated_data['key'] = key

        serializer.save()
