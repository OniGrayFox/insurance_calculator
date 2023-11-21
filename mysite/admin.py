from django.contrib.admin import site
from .models import Category, Prices
# Register your models here.


site.register(Category)
site.register(Prices)