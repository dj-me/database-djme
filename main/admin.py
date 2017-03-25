from django.contrib import admin

from main.models import user , hostsong , djsessions , finalplaylist 


admin.site.register(user)
admin.site.register(hostsong)
admin.site.register(djsessions)
admin.site.register(finalplaylist)
# Register your models here.
