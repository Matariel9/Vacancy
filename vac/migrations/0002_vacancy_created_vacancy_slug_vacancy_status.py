# Generated by Django 4.1.4 on 2023-01-02 07:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('open', 'Открыта'), ('close', 'Закрыта')], default='draft', max_length=6),
        ),
    ]