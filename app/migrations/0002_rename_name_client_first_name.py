# Generated by Django 4.1.6 on 2023-02-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client",
            old_name="name",
            new_name="first_name",
        ),
    ]