# Generated by Django 4.1.4 on 2023-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0006_skill_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
