# Generated by Django 4.2.7 on 2023-11-03 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 3, 11, 31, 24, 319945, tzinfo=datetime.timezone.utc), verbose_name='Дата рождения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]
