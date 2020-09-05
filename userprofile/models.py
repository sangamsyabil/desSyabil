from django.db import models
from accounts.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.user.email

    def get_short_name(self):
        return self.user.email
