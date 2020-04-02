# Generated by Django 3.0.4 on 2020-03-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='customer',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='hardware',
            name='property_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]