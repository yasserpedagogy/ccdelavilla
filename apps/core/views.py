from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from meta.views import Meta
from .models import ContactMessage


def home(request):
    from apps.sermons.models import Sermon
    from apps.blog.models import Post
    from apps.ministries.models import Ministry

    context = {
        "latest_sermons": Sermon.objects.all()[:3],
        "latest_posts": Post.objects.all()[:3],
        "ministries": Ministry.objects.all()[:4],
        "meta": {
            "title": "Comunidad Cristiana de la Villa",
            "description": "Una familia con propósito. Te esperamos para vivir juntos la plenitud del evangelio.",
            "image": "https://ccdelavilla.pythonanywhere.com/static/images/logo.jpg",
        },
    }
    return render(request, "core/home.html", context)


def about(request):
    # Metadatos para la página Acerca de
    meta = Meta(
        title="Acerca de - Comunidad Cristiana de la Villa",
        description="Conoce nuestra historia, visión, creencias y el equipo de liderazgo que forma parte de nuestra comunidad.",
        image="https://ccdelavilla.pythonanywhere.com/static/images/historia.jpg",
        url=request.build_absolute_uri(),
    )

    context = {
        "meta": meta,
    }
    return render(request, "core/about.html", context)


def contact(request):
    if request.method == "POST":
        # Guardar en base de datos
        message = ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone", ""),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        # Enviar email (se verá en consola con EMAIL_BACKEND)
        send_mail(
            f"Mensaje de contacto: {message.subject}",
            f"Nombre: {message.name}\nEmail: {message.email}\nTeléfono: {message.phone}\n\nMensaje:\n{message.message}",
            message.email,  # From
            ["c.c.delavilla@gmail.com"],  # To
            fail_silently=False,
        )

        messages.success(
            request, "¡Mensaje enviado con éxito! Te contactaremos pronto."
        )
        return redirect("core:contact")

    # Metadatos para la página de Contacto
    meta = Meta(
        title="Contacto - Comunidad Cristiana de la Villa",
        description="¿Tienes preguntas? Escríbenos. Estamos aquí para servirte y responder tus inquietudes.",
        image="https://ccdelavilla.pythonanywhere.com/static/images/hero-bg.jpg",
        url=request.build_absolute_uri(),
    )

    context = {
        "meta": meta,
    }
    return render(request, "core/contact.html", context)
