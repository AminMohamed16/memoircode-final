# Generated by Django 3.2.8 on 2022-04-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_remove_person_prenom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='person',
            name='Email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='prenom',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='telephon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
