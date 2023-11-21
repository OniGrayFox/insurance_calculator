from django.shortcuts import render
from .forms import CalculatorForm
from datetime import date
from .models import Category
# Create your views here.
from django.contrib import messages

def index_view(request):
    total = 0
    success = False
    form = CalculatorForm(request.POST)
    if request.POST:
        if form.is_valid():
            success = True
            birth_data = form.cleaned_data['birth_data']
            sports_check = form.cleaned_data['sports_check']
            insurance_sum = form.cleaned_data['insurance_sum']
            insurance_time = form.cleaned_data['insurance_time']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            today = date.today()
            age = today.year - birth_data.year - ((today.month, today.day) < (birth_data.month, birth_data.day))
            if age > 55:
                total += Category.objects.get(name='Страховка пенсионера').price
            if sports_check == 'Профессиональный спорт':
                total += Category.objects.get(name='Профессиональный спорт').price
            else:
                total += Category.objects.get(name='Занятия спортом').price
            if insurance_time == 'весь год':
                total += Category.objects.get(name='весь год').price
            else:
                total += Category.objects.get(name='месяц').price
            if insurance_sum:
                total += int(insurance_sum.price)
            messages.success(request, f"Предварительная сумма страхования: {total}")

    args = {
        'form': form,
        'total': total,
    }
    return render(request, "index.html", args)