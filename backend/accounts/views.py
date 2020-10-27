from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from backend.api.models import TvInfo
from backend.api.pagination import CustomTvInfoPagination
from backend.api.serializers import TvInfoSerializer
from .models import UserProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, UserFavouritesSerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        pk = request.user.pk
        instance = UserProfile.objects.get(pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserFavouritesView(ListAPIView):
    pagination_class = CustomTvInfoPagination
    serializer_class = TvInfoSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        pk = self.request.user.pk
        instance = UserProfile.objects.get(pk=pk).channels.all()
        return instance


class UserFavouritesListView(ListAPIView):
    serializer_class = UserFavouritesSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        pk = self.request.user.pk
        instance = UserProfile.objects.filter(pk=pk)
        return instance