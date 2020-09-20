# Generated by Django 3.1.1 on 2020-09-17 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200917_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='receive',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'CASH'), ('Credit Card', 'CREDIT CARD'), ('Cheque', 'CHEQUE')], default='cash', max_length=20),
        ),
    ]
