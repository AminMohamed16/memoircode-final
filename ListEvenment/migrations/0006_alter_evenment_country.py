# Generated by Django 3.2.8 on 2022-05-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListEvenment', '0005_alter_evenment_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenment',
            name='country',
            field=models.CharField(max_length=100, null=True, verbose_name=map),
        ),
    ]
