# Generated by Django 3.1.1 on 2020-09-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_address_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
