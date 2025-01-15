# Generated by Django 5.1.4 on 2025-01-14 08:00

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0004_alter_score_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='date_year',
            field=models.CharField(choices=[('first_turn', 'First Turn'), ('second_turn', 'Second Turn')], default=builtins.print, max_length=50),
            preserve_default=False,
        ),
    ]
