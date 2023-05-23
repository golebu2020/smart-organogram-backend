from django.contrib import admin
from .models import Director, SeniorManager, Manager, SeniorDeveloper, JuniorDeveloper
# Register your models here.

admin.site.register(Director)
admin.site.register(SeniorManager)
admin.site.register(Manager)
admin.site.register(SeniorDeveloper)
admin.site.register(JuniorDeveloper)


