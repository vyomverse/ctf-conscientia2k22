# Generated by Django 4.1 on 2022-11-06 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='valid',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]