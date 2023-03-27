## UserMgmt 
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext as _
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    username = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = CustomUserManager()

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission,verbose_name=_('user permissions'), blank=True, related_name='custom_user_permissions')

    def __str__(self):
        return self.email

