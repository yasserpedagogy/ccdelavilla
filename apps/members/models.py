from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    baptism_date = models.DateField(null=True, blank=True)
    is_active_member = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="members/", blank=True, null=True)

    class Meta:
        verbose_name = "Perfil de miembro"
        verbose_name_plural = "Perfiles de miembros"

    def __str__(self):
        return f"Perfil de {self.user.username}"


@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        MemberProfile.objects.create(user=instance)
