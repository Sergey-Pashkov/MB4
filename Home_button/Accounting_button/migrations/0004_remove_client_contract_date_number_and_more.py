# Generated by Django 5.0.6 on 2024-06-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting_button', '0003_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='contract_date_number',
        ),
        migrations.RemoveField(
            model_name='client',
            name='organizational_form',
        ),
        migrations.AddField(
            model_name='client',
            name='contract_number_and_date',
            field=models.CharField(blank=True, max_length=255, verbose_name='Дата и номер договора'),
        ),
        migrations.AddField(
            model_name='client',
            name='organization_form',
            field=models.CharField(blank=True, max_length=255, verbose_name='Организационная форма'),
        ),
        migrations.AlterField(
            model_name='client',
            name='comments',
            field=models.TextField(blank=True, default='', verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contact_person',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Контактное лицо'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_price',
            field=models.IntegerField(verbose_name='Цена договора'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='inn',
            field=models.CharField(max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='postal_address',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='Почтовый адрес'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='tax_system',
            field=models.CharField(blank=True, default='-', max_length=255, verbose_name='Система налогообложения'),
            preserve_default=False,
        ),
    ]
