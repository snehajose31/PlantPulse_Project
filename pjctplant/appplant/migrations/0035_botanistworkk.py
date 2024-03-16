# Generated by Django 4.2.6 on 2024-03-14 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appplant', '0034_remove_botanistworks_botanist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotanistWorkk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='botanist_work/')),
                ('botanist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appplant.botprofile')),
            ],
        ),
    ]
