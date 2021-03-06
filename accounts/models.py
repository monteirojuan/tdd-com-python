from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)


class ListUserManager(BaseUserManager):
    def create_user(self, email: str):
        ListUser.objects.create(email=email)

    def create_superuser(self, email: str, password: str):
        self.create_user(email)


class ListUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(primary_key=True)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['email', 'height']

    objects = ListUserManager()

    @property
    def is_staff(self) -> bool:
        return self.email == "juan.monteiro@jmonteiro.net"

    @property
    def is_active(self):
        return True
