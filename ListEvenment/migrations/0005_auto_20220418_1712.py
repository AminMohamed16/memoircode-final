# Generated by Django 3.2.8 on 2022-04-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListEvenment', '0004_evenment_adresse'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenment',
            name='Forme_juridique',
            field=models.CharField(choices=[('SARL', 'SARL'), ('EURL', 'international'), ('AMBASSADE', 'AMBASSADE'), ('ASSOCIATION', 'ASSOCIATION'), ('FEDERATION', 'FEDERATION'), ('MINISTERE', 'MINISTERE'), ('ARTISAN', 'ARTISAN'), ('CHAMBRE', 'CHAMBRE'), ('SPA', 'SPA')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='evenment',
            name='Télephone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
