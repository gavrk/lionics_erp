# Generated by Django 3.2.5 on 2023-02-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0014_auto_20230225_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardtescontract',
            name='valid_until',
            field=models.DateField(default='25.02.2023'),
        ),
    ]
