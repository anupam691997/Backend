from django.db import models
from django.contrib.auth.models import User


class ApiKey(models.Model):
    apikey = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_key')

    def __str__(self):
        return self.apikey


class AndroidApp(models.Model):
    app_name = models.CharField(max_length=255)
    app_package = models.CharField(max_length=255)
    icon_url = models.URLField()
    apikey = models.ForeignKey(ApiKey,on_delete=models.CASCADE,related_name='android_app')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.app_name


