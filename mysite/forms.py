from django import forms
from .models import Insurance


class CalculatorForm(forms.Form):
    birth_age = forms.CharField()
    sport = forms.CharField()
    insurance_sum = forms.IntegerField()
    all_date = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()


    class Meta:
        model = Insurance