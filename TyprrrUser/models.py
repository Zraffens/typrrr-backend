from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class AccountManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_superuser') is not True or other_fields.get('is_staff') is not True:
            return ValueError('Superuser must be both superuser and staff')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):
        
        if not username:
            raise ValueError(_('you must provide a username.'))

        if not email:
            raise ValueError(_('you must provide an email.'))

        email = self.normalize_email(email)
        other_fields.setdefault('is_active', True)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class TyprrrUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    created = models.DateTimeField(auto_now_add=True)
    races_completed = models.IntegerField(default=0)
    average_speed = models.IntegerField(default=0)
    races_won = models.IntegerField(default=0)
    best_speed = models.IntegerField(default=0)
    key_data = models.TextField(null=True, blank=True)
    is_staff = models.BooleanField(blank=True, default=False)
    is_active = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username
