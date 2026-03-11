from django.shortcuts import render, get_object_or_404
from .models import Sermon


def sermon_list(request):
    sermons = Sermon.objects.all()
    latest_sermon = sermons.first()  # El primer sermón (más reciente)
    context = {
        "sermons": sermons,
        "latest_sermon": latest_sermon,
    }
    return render(request, "sermons/list.html", context)


def sermon_detail(request, pk):
    sermon = get_object_or_404(Sermon, pk=pk)
    return render(request, "sermons/detail.html", {"sermon": sermon})
