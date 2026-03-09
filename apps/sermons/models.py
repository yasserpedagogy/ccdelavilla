from django.db import models
from django.utils import timezone


class Sermon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    speaker = models.CharField(max_length=100, verbose_name="Predicador")
    date_preached = models.DateField(default=timezone.now, verbose_name="Fecha")
    description = models.TextField(verbose_name="Descripción")
    audio_file = models.FileField(upload_to="sermons/audio/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    bible_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="sermons/images/", blank=True, null=True)

    class Meta:
        ordering = ["-date_preached"]
        verbose_name = "Sermón"
        verbose_name_plural = "Sermones"

    def __str__(self):
        return f"{self.title} - {self.speaker}"
