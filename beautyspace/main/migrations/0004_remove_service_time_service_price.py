# Generated by Django 5.0.6 on 2024-06-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='time',
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.TextField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]