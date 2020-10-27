from rest_framework import serializers

from backend.api.serializers import TvInfoSerializer
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        exclude = ("channels",)


class UserFavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("channels",)