# Generated by Django 3.2.8 on 2022-04-28 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commendEvent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list_commandevent',
            old_name='Evenment',
            new_name='ListEvenment',
        ),
    ]