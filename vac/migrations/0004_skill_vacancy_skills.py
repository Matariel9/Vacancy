# Generated by Django 4.1.4 on 2023-01-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0003_vacancy_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='skills',
            field=models.ManyToManyField(to='vac.skill'),
        ),
    ]