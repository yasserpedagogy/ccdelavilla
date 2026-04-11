from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactMessage, HeroConfig


def home(request):
    from apps.sermons.models import Sermon
    from apps.blog.models import Post
    from apps.ministries.models import Ministry

    # Obtener la configuración del Hero (o crear una por defecto)
    hero_config = HeroConfig.objects.first()

    # Si no hay configuración, crear una por defecto (para evitar errores)
    if not hero_config:
        hero_config = HeroConfig.objects.create()

    # Si no tiene imagen, usar la imagen por defecto
    hero_image = (
        hero_config.imagen.url if hero_config.imagen else "/static/images/hero-bg.jpg"
    )

    context = {
        "latest_sermons": Sermon.objects.all()[:3],
        "latest_posts": Post.objects.all()[:3],
        "ministries": Ministry.objects.all()[:4],
        "hero_titulo": hero_config.titulo,
        "hero_subtitulo": hero_config.subtitulo,
        "hero_imagen": hero_image,
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")


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

    return render(request, "core/contact.html")
