# Generated by Django 4.2.6 on 2023-11-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_cotizacion_cliente_alter_cotizacion_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='tipo',
            field=models.CharField(choices=[('Servicio', 'Servicio'), ('Compra', 'Compra')], max_length=125, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='tipo',
            field=models.CharField(choices=[('Servicio', 'Servicio'), ('Compra', 'Compra')], max_length=125, verbose_name='Tipo'),
        ),
    ]
