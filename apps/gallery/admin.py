from django.contrib import admin
from .models import Album, GalleryImage


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "album", "is_featured")
    list_editable = ("is_featured",)
