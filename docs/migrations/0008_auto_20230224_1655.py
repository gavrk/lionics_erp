# Generated by Django 3.2.5 on 2023-02-24 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0007_auto_20230224_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardtescontract',
            name='agent',
        ),
        migrations.RemoveField(
            model_name='standardtescontract',
            name='blank',
        ),
        migrations.RemoveField(
            model_name='standardtescontract',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='standardtescontract',
            name='stamped',
        ),
    ]
