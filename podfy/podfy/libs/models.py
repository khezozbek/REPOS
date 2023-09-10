# in django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# in libs file
from .managers import OwnUsersManage
from django.contrib.auth.models import UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("email address", unique=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    channel_name = models.CharField(max_length=120, blank=True, null=True)
    discription = models.TextField()
    profile_img = models.ImageField(upload_to="profiles/img/")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.name