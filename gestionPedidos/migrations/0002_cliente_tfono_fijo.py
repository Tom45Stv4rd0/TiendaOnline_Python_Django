# Generated by Django 3.2.5 on 2021-07-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tfono_fijo',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
