# Generated by Django 3.2.8 on 2022-04-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListEvenment', '0009_auto_20220428_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenment',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
    ]