"""Form file for editing."""
from django import forms
from imager_profile.models import ImagerProfile


class ProfileForm(forms.ModelForm):
    """Form for photo addition."""

    class Meta:
        """."""
        model = ImagerProfile
        exclude = ['user', 'is_active']
