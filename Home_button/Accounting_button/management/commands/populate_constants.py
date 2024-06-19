from django.core.management.base import BaseCommand
from Accounting_button.models import Constant

class Command(BaseCommand):
    help = 'Populate the Constants table with initial values'

    def handle(self, *args, **kwargs):
        constants = [
            ("Стоимость минуты рабочего времени бухгалтера", 7.29, ""),
            ("Стоимость минуты рабочего времени Главного бухгалтера", 9.36, ""),
            ("Месячный фонд рабочего времени (час.)", 1344, ""),
            ("Накладные расходы за месяц (руб.)", 200000, ""),
            ("Накладные расходы на 1 час фонда рабочего времени (руб.)", 0, "Будет вычислено автоматически"),
        ]

        for name, value, comment in constants:
            Constant.objects.update_or_create(name=name, defaults={'value': value, 'comment': comment})

        self.stdout.write(self.style.SUCCESS('Successfully populated the Constants table'))
