# Generated by Django 3.1.1 on 2020-09-12 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_invoice_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depretiation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.item')),
            ],
        ),
    ]
