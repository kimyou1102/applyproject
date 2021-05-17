from django import forms
from .models import Apply

class CreateApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'age', 'say', 'gender']