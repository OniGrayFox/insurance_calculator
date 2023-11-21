from django import forms
from .models import Insurance, Prices

SPORTS = [
    ('Профессиональный спорт', 'Профессиональный спорт'),
    ('Занятия спортом', 'Занятия спортом'),
]
DATE = [
    ('весь год', 'весь год'),
    ('месяц', 'месяц')
]


class CalculatorForm(forms.Form):
    birth_data = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'rectangle-6', 'type': 'date'
    }))
    sports_check = forms.CharField(widget=forms.Select(choices=SPORTS, attrs={
        'class': 'rectangle-6'
    }))
    sport = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'rectangle-5', 'placeholder': 'Вид спорта'
    }))
   # insurance_sum = forms.IntegerField(widget=forms.ModelChoiceField(queryset=Prices.objects.all()))
    insurance_time = forms.CharField(widget=forms.Select(choices=DATE, attrs={
        'class': 'frame-9'
    }))
    start_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'rectangle-6', 'type': 'date'
    }))
    end_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'rectangle-6', 'type': 'date'
    }))

    def __init__(self,*args, **kwagrs):
        super(CalculatorForm, self).__init__(*args, **kwagrs)
        self.fields['insurance_sum'] = forms.ModelChoiceField(queryset=Prices.objects.all(), widget=forms.Select(attrs={
            'class': 'rectangle-6'
        }
                                                                                                                ))
    # add one more url for Insurance Calculator