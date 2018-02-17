from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Define models here
class Person(models.Model):
    googleID = models.TextField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    cell_phone = models.TextField(null=True, blank=True)
    home_phone = models.TextField(null=True, blank=True)
    work_phone = models.TextField(null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)
    work_address = models.TextField(null=True, blank=True)
    spouse = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    img_url = models.TextField(null=True, blank=True)
    positions = models.TextField(null=True, blank=True)

admin.site.register(Person)

class APIKey(models.Model):
    key = models.TextField(null=True, blank=True)

admin.site.register(APIKey)
