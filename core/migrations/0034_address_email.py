# Generated by Django 3.1.1 on 2020-09-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20200929_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]