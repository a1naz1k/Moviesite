# Generated by Django 5.1.3 on 2024-11-20 06:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksite', '0002_alter_movie_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_country', to='ksite.country'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_director', to='ksite.director'),
        ),
    ]
