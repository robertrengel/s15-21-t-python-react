from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class Doc360UserManager(BaseUserManager):
    def create_user(
        self,
        email,
        password=None,
        # name,
        # first_name,
        # last_name,
        # user_country,
        # is_staff,
        # is_superuser,
        # is_active=True,
        # password=None,
        **extra_fields
    ):
        if not email:
            raise ValueError("Please enter an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            # name=name,
            # first_name=first_name,
            # last_name=last_name,
            # user_country=user_country,
            # is_staff=is_staff,
            # is_superuser=is_superuser,
            # is_active=is_active,
            # last_login=now,
            # date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("user_country", "MX")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be have is_superuser =  True")
        return self.create_user(
            email,
            password=password,
            **extra_fields,
        )
