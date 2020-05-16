from rest_framework import serializers
from .models import TvInfo


class TvInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvInfo
        fields = "__all__"
