# Generated by Django 3.1.4 on 2021-02-28 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210228_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='users/avatars/default/default.png', upload_to='users/avatars'),
        ),
    ]
