# Generated by Django 4.2.6 on 2023-10-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Founder",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Manager",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
