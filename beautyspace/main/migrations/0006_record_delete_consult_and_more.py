# Generated by Django 5.0.6 on 2024-06-09 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_service_date_service_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('inject', 'Инъекционная косметология'), ('aesthetic', 'Эстетическая косметология')], max_length=50, null=True, verbose_name='Тип косметологии')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='Время проведения')),
                ('completed', models.BooleanField(default=False, verbose_name='Выполнена')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Отменена')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Запись на услугу',
                'verbose_name_plural': 'Записи на услуги',
            },
        ),
        migrations.DeleteModel(
            name='Consult',
        ),
        migrations.RemoveField(
            model_name='recordservice',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='RecordService',
        ),
    ]