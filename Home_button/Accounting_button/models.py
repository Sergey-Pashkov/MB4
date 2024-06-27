from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

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

class Constant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name == "Накладные расходы на 1 час фонда рабочего времени (руб.)":
            try:
                monthly_work_hours = Constant.objects.get(name="Месячный фонд рабочего времени (час.)")
                monthly_overheads = Constant.objects.get(name="Накладные расходы за месяц (руб.)")
                self.value = monthly_overheads.value / monthly_work_hours.value
            except Constant.DoesNotExist:
                self.value = 0
        super().save(*args, **kwargs)

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

class WorkType(models.Model):
    CHIEF_ACCOUNTANT = 'Главный бухгалтер'
    ACCOUNTANT = 'Бухгалтер'
    PRICE_CATEGORY_CHOICES = [
        (CHIEF_ACCOUNTANT, 'Главный бухгалтер'),
        (ACCOUNTANT, 'Бухгалтер'),
    ]

    name = models.CharField(max_length=255, default="Название работы")
    time_norm = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    price_category = models.CharField(
        max_length=20,
        choices=PRICE_CATEGORY_CHOICES,
        default=ACCOUNTANT,
    )
    comments = models.TextField(default="Нет комментариев")

    def __str__(self):
        return self.name

# models.py
from django.contrib.auth.models import User


# models.py
from django.conf import settings

from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class UnusualOperationLog(models.Model):
    CHIEF_ACCOUNTANT = 'Главный бухгалтер'
    ACCOUNTANT = 'Бухгалтер'
    PRICE_CATEGORY_CHOICES = [
        (CHIEF_ACCOUNTANT, 'Главный бухгалтер'),
        (ACCOUNTANT, 'Бухгалтер'),
    ]

    operation_content = models.TextField(verbose_name="Содержание операции")
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(600)],
        verbose_name="Продолжительность минут"
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    inn = models.CharField(max_length=12, verbose_name="ИНН", editable=False)  # Новое поле
    price_category = models.CharField(
        max_length=20,
        choices=PRICE_CATEGORY_CHOICES,
        verbose_name="Ценовая категория"
    )
    operation_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость операции")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время записи")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")

    def save(self, *args, **kwargs):
        if self.price_category == self.CHIEF_ACCOUNTANT:
            cost_per_minute = Constant.objects.get(name="Стоимость минуты рабочего времени Главного бухгалтера").value
        elif self.price_category == self.ACCOUNTANT:
            cost_per_minute = Constant.objects.get(name="Стоимость минуты рабочего времени бухгалтера").value
        else:
            cost_per_minute = 0

        self.operation_cost = cost_per_minute * self.duration_minutes

        # Автоматически заполняем поле inn из модели Client
        self.inn = self.client.inn

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.operation_content} - {self.client} at {self.timestamp}'


from django.db import models
from django.conf import settings


class StandardOperationLog(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    worktype = models.ForeignKey(WorkType, on_delete=models.CASCADE, verbose_name="Вид работы")
    time_norm = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Норма времени", editable=False)
    price_category = models.CharField(max_length=20, verbose_name="Ценовая категория", editable=False)
    cost_per_minute = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость минуты", editable=False)
    operation_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость операции", editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время записи")
    inn = models.CharField(max_length=12, verbose_name="ИНН", editable=False)
    quantity = models.IntegerField(default=1, verbose_name="Количество")

    def save(self, *args, **kwargs):
        # Получаем значение time_norm и price_category из связанного WorkType
        self.time_norm = self.worktype.time_norm
        self.price_category = self.worktype.price_category

        # Получаем стоимость минуты
        if self.price_category == 'Главный бухгалтер':
            self.cost_per_minute = Constant.objects.get(name="Стоимость минуты рабочего времени Главного бухгалтера").value
        elif self.price_category == 'Бухгалтер':
            self.cost_per_minute = Constant.objects.get(name="Стоимость минуты рабочего времени бухгалтера").value

        # Рассчитываем стоимость операции
        self.operation_cost = self.time_norm * self.cost_per_minute * self.quantity

        # Устанавливаем значение ИНН из модели Client
        self.inn = self.client.inn

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.client} - {self.worktype} - {self.timestamp}'


class DeviationLog(models.Model):
    REQUIREMENT = 'Т'
    EQUIPMENT = 'О'
    RAW_MATERIAL = 'С'
    QUALIFICATION = 'К'
    REASON_CHOICES = [
        (REQUIREMENT, 'Т – требования'),
        (EQUIPMENT, 'О – оборудование'),
        (RAW_MATERIAL, 'С – сырье'),
        (QUALIFICATION, 'К – квалификация'),
    ]

    content = models.TextField(verbose_name="Содержание записи")
    reason = models.CharField(max_length=1, choices=REASON_CHOICES, verbose_name="Причина")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент", blank=True, null=True)
    inn = models.CharField(max_length=12, verbose_name="ИНН", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время записи")
    comments = models.TextField(verbose_name="Комментарии", blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.client:
            self.inn = self.client.inn
        super().save(*args, **kwargs)

    def __str__(self):
        return self.content
    
    