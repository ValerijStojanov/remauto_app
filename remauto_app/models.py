from django.db import models

# Create your models here.

from django.db import models
import random
from django.core.validators import MinLengthValidator

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    viber = models.CharField(max_length=20, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    tiktok = models.CharField(max_length=100, blank=True, null=True)
    auth_code = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)], editable=False)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        if self.pk is None:  # Проверяем, что объект новый (еще не сохранен в базе)
            self.auth_code = self.generate_unique_auth_code()
        super().save(*args, **kwargs)

    def generate_unique_auth_code(self):
        while True:
            auth_code = ''.join(random.choices('0123456789', k=6))
            if not Client.objects.filter(auth_code=auth_code).exists():
                return auth_code
