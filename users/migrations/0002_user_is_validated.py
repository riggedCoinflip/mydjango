# Generated by Django 3.1.4 on 2021-02-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_validated',
            field=models.BooleanField(default=False),
        ),
    ]