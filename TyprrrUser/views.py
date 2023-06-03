from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, SAFE_METHODS, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TyprrrUser
from .serializers import UserSerializer, RegisterUserSerializer, UserProfileSerializer
from rest_framework.mixins import UpdateModelMixin


class UserEditPermission(BasePermission):
    message = 'Editing users is restricted to the author only.'
    print(SAFE_METHODS)

    def has_object_permission(self, request, view, user):

        if request.method in SAFE_METHODS:
            return True

        return user == request.user

class UserListView(generics.ListAPIView, UpdateModelMixin):
    queryset = TyprrrUser.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView, UserEditPermission):
     
    queryset = TyprrrUser.objects.all()
    serializer_class = UserSerializer


class UserCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlackListTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CurrentUser(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({
            "id": request.user.id
            })


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
