from django import forms
from .models import Apply


# 모델폼
class CreateApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'age', 'say', 'gender','image']