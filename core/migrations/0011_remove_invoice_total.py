# Generated by Django 3.1.1 on 2020-09-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='total',
        ),
    ]
