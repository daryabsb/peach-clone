# Generated by Django 3.1.2 on 2020-10-06 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20201006_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='to_account',
            new_name='vendor',
        ),
    ]