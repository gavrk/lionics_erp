# Generated by Django 3.2.5 on 2023-02-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_auto_20230219_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyloc',
            name='acting_on',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='bank_name',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='bic',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='company_name',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='company_type',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='corr_acc',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='curr_acc',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='email',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='inn',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='kpp',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='legal_addr',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='ogrn',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='okpo',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='pass_issued_by',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='pass_issued_code',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='pass_issued_date',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='passport_number',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='passport_series',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='person_nom',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='pos_per_acc',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='position_nom',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='postal_addr',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='registration_addr',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='companyloc',
            name='tel',
            field=models.CharField(default='-', max_length=100),
        ),
    ]