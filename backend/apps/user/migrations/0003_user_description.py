# Generated by Django 3.1.5 on 2021-01-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210119_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]