# Generated by Django 4.1.13 on 2024-02-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("asap", "0005_test2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="test2",
            old_name="title",
            new_name="loginID",
        ),
        migrations.AddField(
            model_name="test2",
            name="loginPW",
            field=models.CharField(default="default_password", max_length=200),
            preserve_default=False,
        ),
    ]
