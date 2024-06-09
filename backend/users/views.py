import uuid

from manager.encryption import PasswordUserEncryption
from .serializers import UserSerializer, ProfileSerializer, UserProfileTokenSerializer
from .models import Profile, ProfileCategories, UserProfileToken
from .services import api_encrypt_profile_pin, get_user_from_token
from .tasks import delete_token

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def login_view(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    response = Response({'user': serializer.data}, status=status.HTTP_200_OK)
    response.set_cookie(key='session_token', value=token, httponly=True, samesite='Lax', max_age=2592000)

    return response


@api_view(['POST'])
def signup_view(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        response = Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        response.set_cookie(key='session_token', value=token, httponly=True, samesite='Lax', max_age=2592000)

        return response

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    token_key = request.COOKIES.get('session_token')

    if token_key:
        token = Token.objects.get(key=token_key)
        if not token:
            return Response({'error': 'Token not found'}, status=status.HTTP_401_UNAUTHORIZED)
        token.delete()

        response = Response({'success': True}, status=status.HTTP_200_OK)
        response.delete_cookie('auth_token')

        return response
    else:
        return Response({'error': 'Token not found in cookies'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_session_info_view(request):
    token_key = request.COOKIES.get('session_token')

    if not token_key:
        return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

    token = Token.objects.get(key=token_key)
    if not token:
        return Response({'error': 'Token not found'}, status=status.HTTP_401_UNAUTHORIZED)

    user = token.user
    return Response({'user_id': user.id, 'username': user.username, 'email': user.email},
                    status=status.HTTP_201_CREATED)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pue = PasswordUserEncryption()

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.user = get_user_from_token(request)

    def get_queryset(self):
        return Profile.objects.filter(user=self.user).order_by('-created')

    def perform_create(self, serializer):
        serializer = api_encrypt_profile_pin(serializer, self.user)
        serializer.save()

    def perform_update(self, serializer):
        serializer = api_encrypt_profile_pin(serializer, self.user)
        serializer.save()


@api_view(['POST'])
def check_profile_pin_view(request):
    pue = PasswordUserEncryption()
    profile_id = request.data['profile_id']
    pin = request.data['pin']

    hashed_pin = get_object_or_404(Profile, id=profile_id).pin
    check_result = pue.check_password(pin, hashed_pin)

    if not check_result:
        return Response({'error': 'Provided pin is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'Token': 'test_token'})


@api_view(['POST'])
def enter_profile_view(request):
    user = request.user
    profile_id = request.data.get('profile_id')

    profile = get_object_or_404(Profile, id=profile_id, user=user)

    UserProfileToken.objects.filter(user=user, profile=profile).delete()

    token = str(uuid.uuid4())
    user_profile_token = UserProfileToken.objects.create(
        user=user,
        profile=profile,
        token=token
    )

    delete_token.apply_async((user_profile_token.id,), countdown=1800)

    return Response({'token': token}, status=status.HTTP_201_CREATED)
