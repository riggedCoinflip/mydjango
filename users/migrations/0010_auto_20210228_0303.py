# Generated by Django 3.1.4 on 2021-02-28 02:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210228_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='github_name',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
    ]
