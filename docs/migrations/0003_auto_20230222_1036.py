# Generated by Django 3.2.5 on 2023-02-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0002_standardtescontract_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardtescontract',
            name='agent',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='standardtescontract',
            name='customer',
            field=models.CharField(default='-', max_length=100),
        ),
    ]