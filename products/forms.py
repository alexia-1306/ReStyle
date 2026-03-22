from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'
        exclude = ('post_date',)
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'city': 'City',

        }