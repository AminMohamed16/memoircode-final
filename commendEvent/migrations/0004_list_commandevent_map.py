# Generated by Django 3.2.8 on 2022-04-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20220428_1932'),
        ('commendEvent', '0003_list_commandevent_porte'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_commandevent',
            name='map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.data'),
        ),
    ]