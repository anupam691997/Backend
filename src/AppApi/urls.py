
from django.urls import path
from . import views
from rest_framework.authtoken import views as rfviews

app_name = 'AppApi'

urlpatterns = [
    path('login',rfviews.obtain_auth_token),
    path('test',views.test,name = 'test'),
    path('apikey', views.ApiKeyView.as_view(), name='apikey'),
    path('app', views.AndroidAppView.as_view(), name='app'),

]
