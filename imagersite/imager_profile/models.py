from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class ImagerProfile(models.Model):
    """Create user profile."""
    website = models.URLField(max_length=150)
    location = models.CharField(max_length=200, blank=True, null=True)
    fee = models.DecimalField(decimal_places=2, max_digits=6, blank=False)
    camera_choices = [
        ('Nikon', 'Nikon'),
        ('Canon', 'Canon'),
        ('Sony', 'Sony'),
    ]
    camera = models.CharField(
        max_length=5,
        choices=camera_choices,
        default='Nikon',
    )
    service_options = [
        ('Weddings', 'Weddings'),
        ('Birthdays', 'Birthdays'),
        ('School', 'School'),
        ('Family', 'Family'),
        ('Portrait', 'Portrait')
    ]
    services = MultiSelectField(
        max_length=10,
        choices=service_options,
        default='Portrait',
    )
    bio = models.TextField(max_length=1000)
    phone_number = PhoneNumberField()
    photo_styles_options = [
        ('Color', 'Color'),
        ('Black_White', 'Black and White'),
        ('Future', 'Future'),
        ('Western', 'Western'),
        ('Architecture', 'Architecture'),
    ]
    photo_style = MultiSelectField(
        max_length=15,
        choices=photo_styles_options,
        default='Color',
    )
    user = models.OneToOneField(User, related_name='profile')

    is_active = models.BooleanField(default=True)
