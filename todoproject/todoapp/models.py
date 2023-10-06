from django.db import models
from django.utils import timezone


# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.CharField(max_length=250)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name