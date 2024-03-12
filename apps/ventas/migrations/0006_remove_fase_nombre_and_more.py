# Generated by Django 4.2.9 on 2024-03-04 00:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_remove_fase_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fase',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='resultadoanalisis',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='analizada',
        ),
        migrations.AddField(
            model_name='resultadoanalisis',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=500),
            preserve_default=False,
        ),
    ]
