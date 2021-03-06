# Generated by Django 3.1.4 on 2021-02-28 15:32

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210228_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to='users/avatars'),
        ),
    ]
