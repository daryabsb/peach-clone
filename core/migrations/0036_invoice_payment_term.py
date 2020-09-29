# Generated by Django 3.1.1 on 2020-09-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_invoice_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payment_term',
            field=models.CharField(choices=[('cash', 'CASH'), ('Credit Card', 'CREDIT CARD'), ('Cheque', 'CHEQUE')], default='cash', max_length=60),
        ),
    ]
