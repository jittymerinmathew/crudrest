from django.db import models
from django.utils import timezone
from datetime import timedelta


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, related_name='products', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.registration_date < timezone.now() - timedelta(days=60):
            self.is_active = False
        super().save(*args, **kwargs)
