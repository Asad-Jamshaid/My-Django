# Generated by Django 4.2.6 on 2023-10-18 14:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cloudpacer", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="founder",
            name="image",
        ),
        migrations.RemoveField(
            model_name="manager",
            name="image",
        ),
    ]
