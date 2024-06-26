# Generated by Django 5.0.6 on 2024-06-26 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting_button', '0014_alter_standardoperationlog_time_norm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardoperationlog',
            name='price_category',
            field=models.CharField(editable=False, max_length=20, verbose_name='Ценовая категория'),
        ),
        migrations.AlterField(
            model_name='standardoperationlog',
            name='time_norm',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=5, verbose_name='Норма времени'),
        ),
    ]
