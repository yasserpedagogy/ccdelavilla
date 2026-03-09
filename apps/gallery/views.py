from django.shortcuts import render
from .models import GalleryImage, Album


def gallery_index(request):
    albums = Album.objects.all()
    featured = GalleryImage.objects.filter(is_featured=True)[:12]
    recent = GalleryImage.objects.all()[:12]

    context = {
        "albums": albums,
        "featured": featured,
        "recent": recent,
    }
    return render(request, "gallery/index.html", context)
