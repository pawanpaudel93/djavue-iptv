from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin

from .models import TvInfo


list_display = [field.name for field in TvInfo._meta.get_fields()]
list_display.remove('userprofile')
search_fields = [f.name for f in TvInfo._meta.get_fields() if f.auto_created is False]
 
TvInfoAdmin = my_admin = type('MyAdmin', (DjangoQLSearchMixin, admin.ModelAdmin,),
                    {'list_display': list_display, 'ordering': ['id', ],
                     'search_fields': search_fields,
                     'list_per_page': 50,
                     },
                    )

admin.site.register(TvInfo, TvInfoAdmin)
