# Generated by Django 5.0.2 on 2024-02-14 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_side', '0002_rename_service_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]