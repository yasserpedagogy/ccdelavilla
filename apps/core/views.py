from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    from apps.sermons.models import Sermon
    from apps.blog.models import Post
    from apps.ministries.models import Ministry

    context = {
        "latest_sermons": Sermon.objects.all()[:3],
        "latest_posts": Post.objects.all()[:3],
        "ministries": Ministry.objects.all()[:4],
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(
                request, "¡Gracias por contactarnos! Te responderemos a la brevedad."
            )
            return redirect("core:contact")
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})
