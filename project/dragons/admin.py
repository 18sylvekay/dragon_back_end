from django.contrib import admin

from project.dragons.models import Dragon


@admin.register(Dragon)
class DragonAdmin(admin.ModelAdmin):
    pass
