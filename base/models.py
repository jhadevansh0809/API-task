from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager

from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractBaseUser,PermissionsMixin):
    #id:will be auto generated
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS = ['email','dob']

    objects = CustomUserManager()

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class ParagraphItem(models.Model):
    paragraph = models.TextField()
    words = ArrayField(
       models.CharField(max_length=50),
       size=1000
   )
