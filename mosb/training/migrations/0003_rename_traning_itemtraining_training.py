# Generated by Django 3.2.7 on 2021-09-16 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20210916_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemtraining',
            old_name='traning',
            new_name='training',
        ),
    ]
