from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, TimeStampedModel):
    mobile = models.CharField(max_length=128, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        """Returns the username of the User when it is printed in the console"""
        return self.username


class Customer(models.Model):
    profile_number = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
