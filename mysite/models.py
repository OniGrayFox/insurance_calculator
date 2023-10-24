from django.db import models



class Category(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=150)
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Категория страхования'
        verbose_name_plural = 'Категории страхования'




class Insurance(models.Model):
