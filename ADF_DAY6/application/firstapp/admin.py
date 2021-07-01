from django.contrib import admin
from .models import request_info,response_info

# Register your models here.
# admin.site.register(news)
admin.site.register(request_info)
admin.site.register(response_info)
# admin.site.register(sport)