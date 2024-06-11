from django.contrib import admin

from .models import UserProfile, Service, ProcedureRecord, Blog

admin.site.register(UserProfile)
admin.site.register(Service)
admin.site.register(ProcedureRecord)
admin.site.register(Blog)
