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

# models.py
class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование", blank=False, null=False)
    org_form = models.CharField(max_length=255, verbose_name="Организационная форма", blank=True, null=True)
    inn = models.CharField(max_length=12, verbose_name="ИНН", blank=False, null=False)
    contract_price = models.IntegerField(verbose_name="Цена договора", blank=False, null=False)
    tax_system = models.CharField(max_length=255, verbose_name="Система налогообложения", blank=True, null=True)
    contract_details = models.CharField(max_length=255, verbose_name="Дата и номер договора", blank=True, null=True)
    contact_person = models.CharField(max_length=255, verbose_name="Контактное лицо", blank=False, null=False)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=False, null=False)
    email = models.EmailField(verbose_name="Электронная почта", blank=False, null=False)
    postal_address = models.CharField(max_length=255, verbose_name="Почтовый адрес", blank=False, null=False)
    comments = models.TextField(verbose_name="Комментарии", blank=True, null=True)

    def __str__(self):
        return self.name
