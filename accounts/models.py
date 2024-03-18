from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
import uuid

def validate_username(value):
    # Your custom validation logic here
    # For example, ensure the username does not contain special characters
    # if not value.isalnum():
    #     raise ValidationError("Username must contain only alphanumeric characters.")
    pass

class User(AbstractUser):
    # Define your custom fields
    number = models.CharField(max_length=10)

    # Customize the username field
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],  # Apply your custom validator
    )

    def __str__(self):
        return self.username
