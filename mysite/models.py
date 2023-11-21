from django.db import models
from django.utils import timezone


class Prices(models.Model):
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'{self.price}'

class Category(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=150)
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Категория страхования'
        verbose_name_plural = 'Категории страхования'

    def __str__(self):
        return self.name

# TODO Добавить поля для агрегации для подсчета общей суммы страховки через MANY-TO-MANY
class Insurance(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=150)
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    patronymic = models.CharField(verbose_name="Отчество", max_length=150)
    email = models.EmailField(verbose_name="E-mail", max_length=150)
    category = models.OneToOneField(Category,verbose_name=Category._meta.verbose_name, on_delete=models.CASCADE)
    date_of_conclusion = models.DateField(verbose_name="Дата заключения")
    date_of_expire = models.DateField(verbose_name="Дата окончания")
    phone_number = models.IntegerField(verbose_name="Номер телефона")



    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховка'

    def __str__(self):
        return self.surname


class News(models.Model):
    headline = models.CharField(verbose_name="Заголовок", max_length=150)
    text = models.TextField(verbose_name="Текст новости")
    image = models.FileField(verbose_name="Фото новости")
    date = models.DateField(verbose_name="Дата размещения новости")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.headline


class QuestionCategory(models.Model):
    name = models.CharField(verbose_name='Наименование вопроса', max_length=150)

    class Meta:
        verbose_name = "Категория вопроса"
        verbose_name_plural = "Категории вопроса"


# CHOICES TO CATEGORY WITH ADD
class Question(models.Model):
    category = models.OneToOneField(QuestionCategory, verbose_name=QuestionCategory._meta.verbose_name, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст вопроса")
    surname = models.CharField(verbose_name="Фамилия", max_length=150)
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    patronymic = models.CharField(verbose_name="Отчество", max_length=150)


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.category


# SPORT_KIND = [
#     ("Любительский спорт", "Любительский спорт"),
#     ("Профессиональный спорт", "Профессиональный спорт")
#
# ]
# class Sports
#
# class Calculator(models.Model):
#     birth_data = models.DateField(verbose_name="Дата рождения")
#     sport = models.CharField()