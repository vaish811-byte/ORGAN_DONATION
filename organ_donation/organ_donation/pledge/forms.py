from django import forms
from .models import Donor, Recipient

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'age', 'email', 'phone', 'organs']

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'age', 'required_organ', 'hospital_name', 'hospital_address', 'urgency_level', 'contact']
