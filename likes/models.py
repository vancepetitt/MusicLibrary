import numbers
from django.db import models

# Create your models here.
class LikeCounter(models.Model):
    like_count = models.IntegerField()