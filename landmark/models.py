from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Landmark(models.Model):
    imgfile = models.FileField(null=True, upload_to="", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)