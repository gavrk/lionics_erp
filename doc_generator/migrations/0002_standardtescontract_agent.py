# Generated by Django 3.2.5 on 2023-02-20 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_ownloc'),
        ('doc_generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardtescontract',
            name='agent',
            field=models.ForeignKey(default='some', on_delete=django.db.models.deletion.CASCADE, to='companies.ownloc'),
            preserve_default=False,
        ),
    ]
