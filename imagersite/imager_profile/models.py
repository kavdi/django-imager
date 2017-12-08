"""Models for imager profile."""
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

from phonenumber_field.modelfields import PhoneNumberField
import uuid

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class ImagerProfile(models.Model):
    """Create user profile."""
    website = models.URLField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, default='')
    fee = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)
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
        max_length=50,
        choices=service_options,
        default='Portrait',
    )
    bio = models.TextField(max_length=1000, blank=True, default='')
    phone_number = PhoneNumberField(blank=True, default='')
    photo_styles_options = [
        ('Color', 'Color'),
        ('Black_White', 'Black and White'),
        ('Future', 'Future'),
        ('Western', 'Western'),
        ('Architecture', 'Architecture'),
    ]
    photo_style = MultiSelectField(
        max_length=50,
        choices=photo_styles_options,
        default='Color',
    )
    user = models.OneToOneField(User, related_name='profile')
    # user_id = models.UUIDField(default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def attach_photographer(sender, **kwargs):
    """Save the user model."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
