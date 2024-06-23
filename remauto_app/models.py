from django.db import models
import random
from django.core.validators import MinLengthValidator, RegexValidator

class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=30, blank=False, unique=True,validators=[
        RegexValidator(
            regex=r'^\+\d{1,3}\d{6,14}$',
            message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.'
        ),
        MinLengthValidator(7)  # Minimum length for phone number
    ])
    email = models.EmailField(unique=True, blank=False)
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
