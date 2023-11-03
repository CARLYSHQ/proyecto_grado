from django.contrib import admin
from .models import Cliente,Cotizacion,Factura,Recibo
from django.conf import settings



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'direccion', 'correo_electronico', 'celular', 'nit', 'razon_social', 'created_at', 'updated_at')
    search_fields = ('nombre', 'apellidos', 'correo_electronico', 'nit', 'razon_social')
    list_filter = ('created_at', 'updated_at')


@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id_cotizacion', 'cliente', 'get_insumos_names', 'total', 'impuesto', 'created_at', 'updated_at')
    list_filter = ('cliente',)
    search_fields = ['id_cotizacion', 'cliente__nombre', 'created_at']
    readonly_fields = ['id_cotizacion', 'created_at', 'updated_at']
    filter_horizontal = ['insumos']

    def get_insumos_names(self, obj):
        return ', '.join([str(insumo.nombre) for insumo in obj.insumos.all()])

    get_insumos_names.short_description = 'Detalle del acabado'



@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id_factura', 'nit', 'razon_social', 'tipo', 'total', 'created_at', 'updated_at')
    list_filter = ('tipo',)
    search_fields = ['id_factura', 'nit', 'razon_social', 'created_at']
    readonly_fields = ['id_factura', 'created_at', 'updated_at']
    actions_on_top = False

    def has_add_permission(self, request):
        return False




@admin.register(Recibo)
class ReciboAdmin(admin.ModelAdmin):
    list_display = ('id_recibo', 'tipo', 'detalle', 'total', 'created_at', 'updated_at')
    search_fields = ['id_recibo', 'tipo']
    readonly_fields = ['id_recibo', 'created_at', 'updated_at']
    actions_on_top = False

    def has_add_permission(self, request):
        return False
