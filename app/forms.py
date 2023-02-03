from django import forms
from .models import Predict
from django.forms import ModelForm


class PredictForm(forms.ModelForm):
    class Meta:
        model = Predict
        fields = '__all__'

