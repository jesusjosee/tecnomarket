# Generated by Django 3.2 on 2021-04-10 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='brand',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
    ]