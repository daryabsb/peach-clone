# Generated by Django 3.1.2 on 2020-10-01 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20201001_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='balance',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='invoiceitem',
            name='status',
            field=models.CharField(default='unpaid', max_length=30),
        ),
    ]
