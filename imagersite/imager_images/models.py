"""Create Image & Album models."""

from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    """Set up the Photo model."""

    title = models.CharField(max_length=40)
    decription = models.TextField(max_length=500)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    file = models.ImageField(upload_to='')
    published_choices = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Shared', 'Shared'),
    ]
    published = models.CharField(
        max_length=10,
        choices=published_choices)
    user = models.ForeignKey(User, related_name='photos')


class Album(models.Model):
    """Set up the Album model."""

    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now=True)
    published_choices = [
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Shared', 'Shared'),
    ]
    published = models.CharField(
        max_length=10,
        choices=published_choices)
    photos = models.ManyToManyField(Photo, related_name='albums')
    user = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    cover_photo = models.ForeignKey('Photo', related_name='+', blank=True,
                                    null=True)
