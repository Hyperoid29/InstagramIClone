from django.db import models


class UserProfile(models.Model):
    email_or_mobile = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username