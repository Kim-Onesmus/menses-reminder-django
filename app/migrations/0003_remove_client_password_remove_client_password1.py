# Generated by Django 4.1.6 on 2023-02-02 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_name_client_first_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="password",
        ),
        migrations.RemoveField(
            model_name="client",
            name="password1",
        ),
    ]
