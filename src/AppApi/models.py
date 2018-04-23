from django.db import models
from django.contrib.auth.models import User


class ApiKey(models.Model):
    apikey = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_key')

    def __str__(self):
        return str(self.user) + "   " + self.apikey


class Country(models.Model):
    country_name = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.country_name + " " + str(self.country_code)


class AndroidApp(models.Model):
    app_name = models.CharField(max_length=255)
    app_package = models.CharField(max_length=255)
    icon_url = models.URLField()
    country = models.ManyToManyField(Country, related_name='android_app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name


class Banner(models.Model):
    MAYBECHOICE = (
        ('T', 'TOP'),
        ('B', 'BOTTOM')
    )

    description = models.TextField()
    ad_pos = models.CharField(max_length=1, choices=MAYBECHOICE)
    app_name = models.CharField(max_length=255)
    app_package = models.CharField(max_length=255)
    icon_url = models.URLField()
    country = models.ManyToManyField(Country, related_name='banner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name + " " + self.description + " " + self.ad_pos
