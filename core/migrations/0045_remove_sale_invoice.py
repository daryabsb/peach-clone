# Generated by Django 3.1.2 on 2020-10-04 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_sale_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='invoice',
        ),
    ]