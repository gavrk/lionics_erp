# Generated by Django 3.2.5 on 2023-02-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_clientloc_registration_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientloc',
            name='pass_issued_by',
            field=models.CharField(default='default_value', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientloc',
            name='pass_issued_code',
            field=models.CharField(default='default_value', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientloc',
            name='pass_issued_date',
            field=models.CharField(default='some', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientloc',
            name='passport_number',
            field=models.CharField(default='default', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientloc',
            name='passport_series',
            field=models.CharField(default='series', max_length=250),
            preserve_default=False,
        ),
    ]
