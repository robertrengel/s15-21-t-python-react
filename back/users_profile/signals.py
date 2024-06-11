from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Doc360User
from users_profile.models import UserProfile


@receiver(post_save, sender=Doc360User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_id=instance.pk, status="T")


@receiver(post_save, sender=Doc360User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
