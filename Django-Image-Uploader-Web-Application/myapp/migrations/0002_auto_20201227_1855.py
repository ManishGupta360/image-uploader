# Generated by Django 3.1.4 on 2020-12-28 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageuploader',
            old_name='data',
            new_name='date',
        ),
    ]