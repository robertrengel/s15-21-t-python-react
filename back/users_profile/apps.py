from django.apps import AppConfig


class UsersProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users_profile"
    verbose_name = "users_profile"

    def ready(self):
        from users_profile import signals
