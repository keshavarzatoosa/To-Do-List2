from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def set_staff_superuser_flags(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.is_staff = True
        instance.save()