from rest_framework import serializers
from .models import ApiKey


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ('apikey',)


class AndroidAppSerializer(serializers.Serializer):
    app_name = serializers.CharField(max_length=255)
    app_package = serializers.CharField(max_length=255)
    apikey = serializers.CharField(max_length=255)
    icon_url = serializers.URLField()


