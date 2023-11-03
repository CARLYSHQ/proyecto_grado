from django.db import models
import uuid
import shortuuid
from apps.compras.models import Insumo


def conver_encode():
    u = uuid.uuid4()
    s = shortuuid.encode(u)
    return s


class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True,max_length=100,unique=True,default=conver_encode,editable=False)
    nombre = models.CharField(max_length=155, blank=False, null=False,verbose_name="Nombres")
    apellidos = models.CharField(max_length=255, blank=False, null=False,verbose_name="Apellidos")
    direccion = models.CharField(max_length=255, blank=True, null=True,verbose_name="Direccion")
    correo_electronico = models.EmailField(max_length=255, blank=False, null=False,verbose_name="Correo Electrónico")
    celular = models.CharField(max_length=255, blank=True, null=True,verbose_name="Número de celular")
    nit = models.CharField(max_length=55, blank=True, null=True,verbose_name="NIT")
    razon_social = models.CharField(max_length=255, blank=True, null=True,verbose_name="Razón social")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre+' '+self.apellidos
    
    class Meta():
        verbose_name="Cliente"
        verbose_name_plural="Clientes"
        db_table="cliente"


class Cotizacion(models.Model):
    id_cotizacion = models.CharField(primary_key=True, max_length=100, unique=True, default=conver_encode, editable=False)
    cliente = models.ForeignKey(Cliente, blank=True, null=True, related_name="cotizaciones", on_delete=models.CASCADE, verbose_name="Cliente")
    insumos = models.ManyToManyField(Insumo, verbose_name="Insumos")
    total = models.FloatField(default=0, blank=False, null=False, verbose_name="Total de la cotizacion",editable=False)
    impuesto = models.IntegerField(default=0, blank=False, null=False, verbose_name="Impuesto (%)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_cotizacion

    def save(self, *args, **kwargs):
        # Calcula la suma de los precios de los insumos asociados a la cotización
        suma_precios = sum(insumo.precio for insumo in self.insumos.all())
        print(f"Suma de precios antes de impuesto: {suma_precios}")

        # Si hay impuesto, suma el impuesto al total
        if self.impuesto > 0:
            impuesto_calculado = (suma_precios * self.impuesto) / 100
            print(f"Impuesto calculado: {impuesto_calculado}")
            self.total = suma_precios + impuesto_calculado
        else:
            # Si no hay impuesto, suma directamente los precios de los insumos
            self.total = suma_precios

        # Llama al método save() del modelo base para guardar los cambios
        super().save(*args, **kwargs)

    class Meta():
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"
        db_table = "cotizacion"


CHOICES_TIPO=[
    ('Servicio','Servicio'),
    ('Compra','Compra'),
]


class Factura(models.Model):
    id_factura = models.CharField(primary_key=True,max_length=100,unique=True,default=conver_encode,editable=False)
    nit = models.CharField(max_length=55, blank=True, null=True,verbose_name="NIT")
    razon_social = models.CharField(max_length=255, blank=True, null=True,verbose_name="Razón social")
    tipo = models.CharField(max_length = 125,verbose_name="Tipo",choices=CHOICES_TIPO,blank=False,null=False)
    detalle = models.TextField(max_length=800, blank=True, null=True,verbose_name="Detalle")
    total=models.FloatField(blank=False,null=False,verbose_name="Total")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_compra
    
    
    class Meta():
        verbose_name="Factura"
        verbose_name_plural="Facturas"
        db_table="factura"


CHOICES_TIPO=[
    ('Servicio','Servicio'),
    ('Compra','Compra'),
]


class Recibo(models.Model):
    id_recibo = models.CharField(primary_key=True,max_length=100,unique=True,default=conver_encode,editable=False)
    tipo = models.CharField(max_length = 125,verbose_name="Tipo",choices=CHOICES_TIPO,blank=False,null=False)
    detalle = models.TextField(max_length=800, blank=True, null=True,verbose_name="Detalle")
    total=models.FloatField(blank=False,null=False,verbose_name="Total")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_compra
    
    
    class Meta():
        verbose_name="Recibo"
        verbose_name_plural="Recibos"
        db_table="recibo"