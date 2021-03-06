# Generated by Django 3.1.1 on 2020-10-01 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_invoice_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(default='unpaid', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]
