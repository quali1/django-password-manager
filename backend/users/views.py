from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


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


@api_view(['GET'])
def test_token_view(request):
    return Response({})


@api_view(['POST'])
def logout_view(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user:
        return Response({'error': 'Not found'}, status=status.HTTP_400_BAD_REQUEST)

    token = Token.objects.get(user=user)
    token.delete()
    return Response({'success': True}, status=status.HTTP_200_OK)
