from django.db import models
from django.contrib.auth.models import AbstractUser

class Word(models.Model):
    text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.translation}"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

# Create your models here.
