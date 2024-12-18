from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('landlord', 'Landlord'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
 
 
class Apartment(models.Model):
    rooms = models.IntegerField()
    new_construction = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.CharField(max_length=255, blank=True)
    size = models.IntegerField()
    university = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.location} - {self.rooms} rooms - ${self.price}"
