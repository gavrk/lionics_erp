# Generated by Django 3.2.5 on 2023-02-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_companyloc_company_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyloc',
            name='company_type',
            field=models.CharField(max_length=100),
        ),
    ]
