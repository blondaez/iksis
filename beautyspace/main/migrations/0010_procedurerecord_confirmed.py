# Generated by Django 5.0.6 on 2024-06-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_procedurerecord_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedurerecord',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Подтверждено администратором'),
        ),
    ]
