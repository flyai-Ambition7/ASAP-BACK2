# Generated by Django 4.1.13 on 2024-02-15 06:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("asap", "0012_rename_user_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="call_num",
            new_name="phone",
        ),
    ]
