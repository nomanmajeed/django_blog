from django.db import models
from django.contrib.auth.models import User
from common.models import TimeStampedModel

class Profile(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)