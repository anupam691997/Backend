from rest_framework import serializers
from .models import ApiKey, Banner, Country, AndroidApp


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ('apikey',)


class AndroidAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AndroidApp
        fields = ('app_name', 'app_package', 'icon_url')

    def create(self, validated_data):
        app = AndroidApp()
        app.app_name = validated_data['app_name']
        app.app_package = validated_data['app_package']
        app.icon_url = validated_data['icon_url']
       # app.country = validated_data['country']

        app.save()
        return app


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ('app_name', 'app_package', 'icon_url', 'description', 'ad_pos')

    def create(self, validated_data):
        banner = Banner()
        banner.app_name = validated_data['app_name']
        banner.app_package = validated_data['app_package']
        banner.icon_url = validated_data['icon_url']
        #banner.country = validated_data['country']
        banner.description = validated_data['description']
        banner.ad_pos = validated_data['ad_pos']

        banner.save()
        return banner


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_name', 'country_code')
