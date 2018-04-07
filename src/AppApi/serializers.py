from rest_framework import serializers
from .models import ApiKey,Banner


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ('apikey',)


class AndroidAppSerializer(serializers.Serializer):
    app_name = serializers.CharField(max_length=255)
    app_package = serializers.CharField(max_length=255)
    apikey = serializers.CharField(max_length=255)
    icon_url = serializers.URLField()


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('app_name','app_package','icon_url','description','ad_pos')

    def create(self, validated_data):

        banner = Banner()
        banner.app_name=validated_data['app_name']
        banner.app_package=validated_data['app_package']
        banner.icon_url=validated_data['icon_url']
        banner.apikey=validated_data['apikey']
        banner.description=validated_data['description']
        banner.ad_pos=validated_data['ad_pos']

        banner.save()
        return banner