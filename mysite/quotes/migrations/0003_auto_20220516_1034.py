# Generated by Django 2.2.4 on 2022-05-16 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_list'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Symbol',
            new_name='Stock',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='symbol',
            new_name='ticker',
        ),
    ]
