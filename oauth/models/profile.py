from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profiles', verbose_name='user')
    first_name = models.CharField(max_length=100, blank=True, verbose_name='first name')
    last_name = models.CharField(max_length=100, blank=True, verbose_name='last name')
    address = models.CharField(max_length=100, blank=True, verbose_name='address')
    description = models.CharField(max_length=100, blank=True, verbose_name='description')
