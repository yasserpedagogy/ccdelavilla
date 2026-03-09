from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Contenido")
    excerpt = models.TextField(max_length=300, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

    class Meta:
        ordering = ["-published_date"]
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
