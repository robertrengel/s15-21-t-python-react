from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import ApiUser
from users_profile.models import UserProfile


@receiver(post_save, sender=ApiUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_id=instance.pk, status="T")


@receiver(post_save, sender=ApiUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
