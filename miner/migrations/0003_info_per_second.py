# Generated by Django 5.0.6 on 2024-06-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("miner", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="info",
            name="per_second",
            field=models.IntegerField(default=1, verbose_name="point_per_second"),
        ),
    ]
