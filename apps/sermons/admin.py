from django.contrib import admin
from .models import Sermon


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ("title", "speaker", "date_preached")
    list_filter = ("speaker", "date_preached")
    search_fields = ("title", "speaker")
