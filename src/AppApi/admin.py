from django.contrib import admin
from .models import ApiKey,AndroidApp,Banner
from .models import Country

#admin.site.register(ApiKey)
admin.site.register(AndroidApp)
admin.site.register(Banner)
admin.site.register(Country)


