# Generated by Django 3.1.2 on 2020-10-06 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20201006_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]