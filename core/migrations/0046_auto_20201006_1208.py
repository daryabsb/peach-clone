# Generated by Django 3.1.2 on 2020-10-06 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_accounttemplate_balance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='balance',
            new_name='total',
        ),
        migrations.CreateModel(
            name='VendorInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('payment_term', models.CharField(choices=[('cash', 'CASH'), ('Credit Card', 'CREDIT CARD'), ('Cheque', 'CHEQUE')], default='cash', max_length=60)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('invoked', 'INVOKED'), ('paid', 'PAID')], default='pending', max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendor')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]