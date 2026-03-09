from django.db import models


class Ministry(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ministerio")
    description = models.TextField(verbose_name="Descripción")
    leader = models.CharField(max_length=100, verbose_name="Líder")
    meeting_time = models.CharField(max_length=100, blank=True)
    meeting_location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="ministries/", blank=True, null=True)
    icon_class = models.CharField(max_length=50, default="fa-heart")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Ministerio"
        verbose_name_plural = "Ministerios"

    def __str__(self):
        return self.name
