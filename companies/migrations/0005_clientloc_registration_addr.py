# Generated by Django 3.2.5 on 2023-02-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_clientloc_company_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientloc',
            name='registration_addr',
            field=models.CharField(default='some_addr', max_length=500),
            preserve_default=False,
        ),
    ]