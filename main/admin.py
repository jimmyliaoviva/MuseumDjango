from django.contrib import admin
from .models import City, Nation, Museum


# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('cid', 'cname', 'nation')


admin.site.register(City, CityAdmin)
admin.site.register(Nation)
admin.site.register(Museum)
