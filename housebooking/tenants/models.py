from django.db import models
import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


#Unique ID Generator
ID_CHOICES = (
    ('NIN', 'NIN'),
    ('VIN', "Voter's Card Num"),
)

#Tenant's Registration Form
class Tenant(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=16, choices=ID_CHOICES)
    id_number = models.CharField(max_length=20)
    DOB = models.DateField()

    def __str__(self):
        return f"{self.tenant.first_name} {self.tenant.last_name}"
