# Generated by Django 3.2.7 on 2021-09-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20210909_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CNPJ'),
        ),
    ]
