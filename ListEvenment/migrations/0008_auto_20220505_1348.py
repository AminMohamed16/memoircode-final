# Generated by Django 3.2.8 on 2022-05-05 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ListEvenment', '0007_alter_evenment_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evenment',
            old_name='date_creation',
            new_name='date_creation_evenment',
        ),
        migrations.AddField(
            model_name='evenment',
            name='date_fine_evenment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
