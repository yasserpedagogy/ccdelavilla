from django.shortcuts import render
from .models import Ministry


def ministry_list(request):
    ministries = Ministry.objects.all()
    return render(request, "ministries/list.html", {"ministries": ministries})
