import datetime
import time
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from service00.models import com_cdh,com_cdd

class com_cdhAdmin(admin.ModelAdmin):
    pass

class com_cddAdmin(admin.ModelAdmin):
	pass

admin.site.register(com_cdh, com_cdhAdmin)   
admin.site.register(com_cdd, com_cddAdmin)   