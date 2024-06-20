from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('accountant', 'Бухгалтер'),
        ('director', 'Директор'),
        ('owner', 'Собственник'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='accountant')

class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models

# Модель для справочника констант
class Constant(models.Model):
    name = models.CharField(max_length=150, unique=True)  # Наименование
    value = models.DecimalField(max_digits=10, decimal_places=2)  # Значение
    comment = models.TextField(blank=True)  # Комментарий

    def __str__(self):
        return self.name

    # Переопределяем метод save для вычисления значения для определенной константы
    def save(self, *args, **kwargs):
        if self.name == "Накладные расходы на 1 час фонда рабочего времени (руб.)":
            try:
                # Получаем необходимые константы для вычисления
                monthly_work_hours = Constant.objects.get(name="Месячный фонд рабочего времени (час.)")
                monthly_overheads = Constant.objects.get(name="Накладные расходы за месяц (руб.)")
                self.value = monthly_overheads.value / monthly_work_hours.value
            except Constant.DoesNotExist:
                self.value = 0
        super().save(*args, **kwargs)

# Create your models here.
from django.db import models

from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Наименование', blank=False)
    organization_form = models.CharField(max_length=255, verbose_name='Организационная форма', blank=True)
    inn = models.CharField(max_length=12, verbose_name='ИНН', blank=False)
    contract_price = models.IntegerField(verbose_name='Цена договора', blank=False)
    tax_system = models.CharField(max_length=255, verbose_name='Система налогообложения', blank=True)
    contract_number_and_date = models.CharField(max_length=255, verbose_name='Дата и номер договора', blank=True)
    contact_person = models.CharField(max_length=255, verbose_name='Контактное лицо', blank=True, default='')
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, default='')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, default='')
    postal_address = models.CharField(max_length=255, verbose_name='Почтовый адрес', blank=True)
    comments = models.TextField(verbose_name='Комментарии', blank=True, default='')

    def __str__(self):
        return self.name
