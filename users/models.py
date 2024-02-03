from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField('Name',max_length=191,null=True) 
    email = models.EmailField('email address', unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank=True,null=True)
    birth_date = models.DateField('Date of Birth',blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username