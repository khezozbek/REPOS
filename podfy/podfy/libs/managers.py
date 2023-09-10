from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class OwnUsersManage(BaseUserManager):
    """
        For manage model when create user
    """
    def create_user(self, email, password, **extra_fields):
        """
            Create and save with email and password.
        """

        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def createsuper_user(self, email, passowrd, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff must be True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser must be True"))
        return self.create_user(email, passowrd, **extra_fields)
