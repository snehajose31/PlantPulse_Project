# Generated by Django 4.2.6 on 2023-10-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appplant', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('CUSTOMER', 'CUSTOMER'), ('BOTANIST', 'BOTANIST'), ('HORTICULTURE', 'HORTICULTURE')], max_length=50),
        ),
    ]