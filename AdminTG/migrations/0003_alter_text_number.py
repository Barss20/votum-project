# Generated by Django 4.2.2 on 2023-06-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminTG', '0002_text_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='number',
            field=models.IntegerField(default='Введите номер', unique=True),
        ),
    ]
