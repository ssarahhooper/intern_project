from django import forms
from .models import Kit
from .models import PostMortem


class KitForm(forms.ModelForm):
    class Meta:
        model = Kit
        fields = ['name', 'current_location', 'destination_location', 'status', 'issues', 'needs_restock']


class PostMortForm(forms.ModelForm):
    class Meta:
        model = PostMortem
        fields = ['kit', 'name', 'event_name', 'event_date', 'summary', 'issues', 'restock']
        KITS = [(f'Kit {i}', f'Kit {i}') for i in range(1, 11)]
        widgets = {
            'kit': forms.Select(choices=KITS, attrs={'class': 'w-full border rounded-md p-2'}),
            'name': forms.TextInput(attrs={'class': 'w-full border rounded-md p-2'}),
            'event_name': forms.TextInput(attrs={'class': 'w-full border rounded-md p-2'}),
            'event_date': forms.DateInput(attrs={'class': 'w-full border rounded-md p-2', 'type': 'date'}),
            'summary': forms.Textarea(attrs={'class': 'w-full border rounded-md p-2', 'rows': 3}),
            'issues': forms.Textarea(attrs={'class': 'w-full border rounded-md p-2', 'rows': 3}),
            'restock': forms.Textarea(attrs={'class': 'w-full border rounded-md p-2', 'rows': 2, 'placeholder': 'List restock items if any, leave blank if none...'}),
        }
