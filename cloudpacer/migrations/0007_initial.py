# Generated by Django 4.2.6 on 2023-10-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cloudpacer", "0006_delete_employee_delete_founder_delete_manager"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.IntegerField()),
            ],
        ),
    ]