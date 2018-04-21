from django.http import HttpResponse
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ApiKey, AndroidApp, Banner
from .serializers import ApiKeySerializer, AndroidAppSerializer, BannerSerializer
import hashlib
from .serializers import CountrySerializer
from .models import Country


def test(request):
    st = get_random_string(32).encode('utf-8')
    hash_object = hashlib.sha256(st)
    hex_dig = hash_object.hexdigest()
    return HttpResponse(hex_dig)


class ApiKeyView(APIView):

    def post(self, request):
        st = get_random_string(32).encode('utf-8')
        hash_object = hashlib.sha256(st)
        hex_dig = hash_object.hexdigest()
        object = ApiKey.objects.create(user=request.user, apikey=hex_dig)
        serializer = ApiKeySerializer(object, many=False)

        return Response(serializer.data)

    def get(self, request):
        keys = ApiKey.objects.filter(user=request.user)
        serializer = ApiKeySerializer(keys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AndroidAppView(APIView):

    def post(self, request):

        serializer1 = AndroidAppSerializer(data=request.data, many=False)

        serializer1.is_valid(raise_exception=True)

        country_name = request.data.get('country_name', 'none')
        country_code = request.data.get('country_code', 'none')

        try:
            obj = Country.objects.get(country_name=country_name, country_code=country_code)
        except:
            return Response({'error': 'no such country exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            serializer1.save(country=obj)
        except:
            return Response({'error': 'object could not be created'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(request.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        country_name = request.GET.get('country_name', 'no_key_passed')
        country_code = request.GET.get('country_code', 'no_key_passed')

        try:
            obj = Country.objects.get(country_name=country_name, country_code=country_code)
        except:
            return Response({'error': 'no such country exists'})

        apps = AndroidApp.objects.filter(country=obj)
        serializer = AndroidAppSerializer(apps, many=True)
        return Response(serializer.data)


class BannerView(APIView):

    def post(self, request):

        serializer1 = BannerSerializer(data=request.data, many=False)

        serializer1.is_valid(raise_exception=True)

        country_name = request.data.get('country_name', 'none')
        country_code = request.data.get('country_code', 'none')

        try:
            obj = Country.objects.get(country_name=country_name, country_code=country_code)
        except:
            return Response({'error': 'no such country exists'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            serializer1.save(country=obj)
        except:
            return Response({'error': 'object could not be created'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(request.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        country_name = request.GET.get('country_name', 'no_key_passed')
        country_code = request.GET.get('country_code', 'no_key_passed')

        try:
            obj = Country.objects.get(country_name=country_name, country_code=country_code)
        except:
            return Response({'error': 'no such country exists'})

        banner = Banner.objects.filter(country=obj)
        serializer = BannerSerializer(banner, many=True)
        return Response(serializer.data)


class CountryView(APIView):

    def post(self, request):
        serializer = CountrySerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except:
            return Response({'error': 'could not save'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
