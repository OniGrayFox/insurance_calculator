from django import forms
from .models import Insurance


class CalculatorForm(forms.Form):
    birth_age = forms.CharField()
    sport = forms.CharField()
    insurance_sum = forms.IntegerField()
    insurance_time = forms.CharField()
    start_date = forms.DateField()
    end_date = forms.DateField()


    # add one more url for Insurance Calculator