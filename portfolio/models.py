from typing import Any
from django.db import models

# Create your models here.
class Contact(models.Model):
    fullName=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.fullName + " " + self.subject