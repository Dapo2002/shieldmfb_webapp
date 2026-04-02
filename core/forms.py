from django import forms
from .models import LoanApplication

class LoanForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['full_name', 'email', 'loan_amount', 'purpose']