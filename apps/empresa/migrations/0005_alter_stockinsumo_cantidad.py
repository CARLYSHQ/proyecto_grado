# Generated by Django 4.2.6 on 2023-11-03 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_remove_inventario_cantidad_stockinsumo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockinsumo',
            name='cantidad',
            field=models.IntegerField(default=0, verbose_name='Cantidad en stock'),
        ),
    ]