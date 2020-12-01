from django.contrib import admin
from .models import image

admin.site.site_header = "DBC-Photos Admin"
admin.site.site_title = "DBC-Photos Admin Area"
admin.site.index_title = "Welcom to DBC-Photos Admin Area"

admin.site.register(image)
