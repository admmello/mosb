# Generated by Django 3.2.7 on 2021-09-06 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]