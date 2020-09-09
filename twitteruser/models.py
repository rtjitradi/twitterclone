from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
# https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
# https://stackoverflow.com/questions/36852324/in-django-what-does-symmetrical-true-do
class CustomUserModel(AbstractUser):
    follow = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

    @property
    def display_name(self):
        return self.first_name + '' + self.last_name
