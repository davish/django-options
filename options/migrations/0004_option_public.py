# Generated by Django 3.0.3 on 2020-02-28 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("options", "0003_auto_20181101_2050"),
    ]

    operations = [
        migrations.AddField(
            model_name="option",
            name="public",
            field=models.BooleanField(default=True),
        ),
    ]
