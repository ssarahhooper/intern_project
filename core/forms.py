from django import forms
from .models import Kit


class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ['name', 'current_location', 'destination', 'status', 'issues', 'needs_restock']