from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('accountant', 'Бухгалтер'),
        ('director', 'Директор'),
        ('owner', 'Собственник'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='accountant')

class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
