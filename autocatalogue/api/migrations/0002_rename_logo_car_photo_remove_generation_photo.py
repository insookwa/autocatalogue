# Generated by Django 4.1.7 on 2023-04-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='logo',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='generation',
            name='photo',
        ),
    ]
