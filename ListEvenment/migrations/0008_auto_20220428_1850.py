# Generated by Django 3.2.8 on 2022-04-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListEvenment', '0007_rename_forme_juridique_evenment_organisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenment',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evenment',
            name='date_creation',
            field=models.DateTimeField(null=True),
        ),
    ]