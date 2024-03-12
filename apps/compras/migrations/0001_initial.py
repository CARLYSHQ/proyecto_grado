# Generated by Django 4.2.6 on 2023-11-02 16:37

import apps.compras.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.CharField(default=apps.compras.models.conver_encode, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('total_compra', models.FloatField(default=0, editable=False, verbose_name='Total de la compra')),
                ('factura', models.BooleanField(default=False, verbose_name='Facturado')),
                ('impuesto_iva', models.IntegerField(default=13, editable=False, verbose_name='IMPUESTO IVA %')),
                ('impuesto_it', models.IntegerField(default=3, editable=False, verbose_name='IMPUESTO IT %')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='empresa.inventario', verbose_name='Inventario')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.CharField(default=apps.compras.models.conver_encode, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=155, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('correo_electronico', models.EmailField(max_length=255, verbose_name='Correo Electrónico')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Número de celular')),
                ('nit', models.CharField(blank=True, max_length=55, null=True, verbose_name='NIT')),
                ('razon_social', models.CharField(blank=True, max_length=255, null=True, verbose_name='Razón social')),
                ('latitud', models.CharField(blank=True, max_length=55, null=True, verbose_name='Latitud')),
                ('longitud', models.CharField(blank=True, max_length=55, null=True, verbose_name='Longitud')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Insumo',
            fields=[
                ('id_insumo', models.CharField(default=apps.compras.models.conver_encode, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=155, verbose_name='Nombre')),
                ('detalle', models.TextField(blank=True, max_length=500, null=True, verbose_name='Detalle')),
                ('categoria', models.CharField(choices=[('Materiales de Impresion', 'Materiales de Impresion'), ('Herramientas y Equipos', 'Herramientas y Equipos'), ('Partes y Accesorios', 'Partes y Accesorios'), ('Embalaje', 'Embalaje')], max_length=125, verbose_name='Categoria')),
                ('precio', models.FloatField(default=0, verbose_name='Precio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insumos', to='compras.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
                'db_table': 'insumo',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id_detalle_compra', models.CharField(default=apps.compras.models.conver_encode, editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('compra', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='compras.compra', verbose_name='Compra')),
                ('insumo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_compra', to='compras.insumo', verbose_name='Insumo')),
            ],
            options={
                'verbose_name': 'Detalle de la Compra',
                'verbose_name_plural': 'Detalles de las Compras',
                'db_table': 'detalle_compra',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='compras.proveedor', verbose_name='Proveedor'),
        ),
    ]