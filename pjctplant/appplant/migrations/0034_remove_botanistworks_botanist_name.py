# Generated by Django 4.2.6 on 2024-03-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appplant', '0033_botanistworks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botanistworks',
            name='botanist_name',
        ),
    ]
