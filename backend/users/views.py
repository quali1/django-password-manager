from manager.encryption import PasswordUserEncryption
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        pue = PasswordUserEncryption()

        pin = serializer.validated_data['pin']
        hashed_pin = pue.encrypt_password(pin)

        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['pin'] = hashed_pin

        return serializer.save()


@api_view(['POST'])
def login_view(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, 'user': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user:
        return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

    token = Token.objects.get(user=user)
    token.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)
