# Generated by Django 3.2.5 on 2023-02-25 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_ownloc'),
        ('docs', '0013_auto_20230225_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardtescontract',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.ownloc'),
        ),
        migrations.AlterField(
            model_name='standardtescontract',
            name='contract_date',
            field=models.DateField(default='25.02.2023'),
        ),
        migrations.AlterField(
            model_name='standardtescontract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.clientloc'),
        ),
        migrations.AlterField(
            model_name='standardtescontract',
            name='stamped',
            field=models.BooleanField(default=False),
        ),
    ]
