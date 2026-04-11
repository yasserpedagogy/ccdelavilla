from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"


# NUEVO MODELO PARA EL HERO DINÁMICO
class HeroConfig(models.Model):
    imagen = models.ImageField(
        upload_to="hero/",
        blank=True,
        null=True,
        verbose_name="Imagen de fondo del Hero",
    )
    titulo = models.CharField(
        max_length=200,
        default="Comunidad Cristiana de la Villa",
        verbose_name="Título principal",
    )
    subtitulo = models.CharField(
        max_length=200,
        default="Viviendo en el poder del evangelio",
        verbose_name="Subtítulo",
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Última actualización"
    )

    class Meta:
        verbose_name = "Configuración del Hero"
        verbose_name_plural = "Configuración del Hero"

    def __str__(self):
        return f"Hero configurado el {self.updated_at}"
