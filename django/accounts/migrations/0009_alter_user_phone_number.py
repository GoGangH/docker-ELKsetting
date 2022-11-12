# Generated by Django 4.0 on 2022-11-07 06:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator('^010-?\\d{4}-?\\d{4}$')]),
        ),
    ]