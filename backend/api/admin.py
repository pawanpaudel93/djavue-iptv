from django.contrib import admin
from .models import TvInfo


class TvInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TvInfo._meta.get_fields()]
    ordering = ['id', ]


admin.site.register(TvInfo, TvInfoAdmin)
