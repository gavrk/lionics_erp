# Generated by Django 3.2.5 on 2023-02-19 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0009_auto_20230219_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardTesContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(default='-', max_length=100)),
                ('contract_date', models.CharField(default='-', max_length=100)),
                ('contract_city', models.CharField(default='-', max_length=250)),
                ('valid_until', models.CharField(default='-', max_length=100)),
                ('blank', models.BooleanField(default=True)),
                ('stamped', models.BooleanField(default=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.clientloc')),
            ],
        ),
    ]
