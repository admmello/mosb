# Generated by Django 3.2.7 on 2021-09-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210906_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.BooleanField(blank=True, default=True, verbose_name='ativo'),
        ),
    ]
