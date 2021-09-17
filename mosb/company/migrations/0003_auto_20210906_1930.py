# Generated by Django 3.2.7 on 2021-09-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
    ]