# Generated by Django 4.2.9 on 2024-03-04 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_remove_fase_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultadoanalisis',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
    ]
