from manager.encryption import PasswordUserEncryption
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, ProfileCategories
from .services import api_encrypt_profile_pin

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pue = PasswordUserEncryption()

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer = api_encrypt_profile_pin(serializer, self.request.user)
        serializer.save()

    def perform_update(self, serializer):
        serializer = api_encrypt_profile_pin(serializer, self.request.user)
        serializer.save()


@api_view(['POST'])
def check_profile_pin_view(request):
    pue = PasswordUserEncryption()
    category_id = request.data['category_id']
    pin = request.data['pin']

    get_object_or_404(ProfileCategories, id=category_id)

    hashed_pin = Profile.objects.get(user=request.user, category=category_id).pin
    check_result = pue.check_password(pin, hashed_pin)

    if not check_result:
        return Response({'error': 'Provided pin is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'Token': 'test_token'})


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
