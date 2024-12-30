from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("Name of User"), max_length=255, blank=True)
    first_name = None
    last_name = None

    def __str__(self) -> str:
        return self.username
