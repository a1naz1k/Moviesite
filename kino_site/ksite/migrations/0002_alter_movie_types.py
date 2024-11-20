# Generated by Django 5.1.3 on 2024-11-20 05:52

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ksite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(144, 144), (360, 360), (480, 480), (720, 720), (1080, 1080)], max_length=20),
        ),
    ]