from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.models import UserManager

class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(blank=False, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_active_datetime = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username

    def update_last_active(self):
        """
        Update the last active datetime for the user
        """
        self.last_active_datetime = timezone.now()
        self.save(update_fields=['last_active_datetime'])
