from django.db import models
from django.core.mail import send_mail
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager



class AccountManager(BaseUserManager):
    def create_user(self, username, email, name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


# class Account(AbstractBaseUser, TimeStampedModel):
class Account(AbstractBaseUser):
    name = models.CharField(max_length=50, default="", unique=True)
    email = models.EmailField(max_length=255, default="", unique=True)

    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return "username: " + self.username
