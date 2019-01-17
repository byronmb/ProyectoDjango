from django.contrib import admin

# Register your models here.
from .models import Cliente

from .models import Cuenta
from .models import Transaccion
from .models import Transferencia




class AdminCliente(admin.ModelAdmin):

    list_display = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
    list_editable = ["apellidos", "nombres", "genero"]
    list_filter = ["genero", "direccion", "fechaNacimiento", "estadoCivil"]
    search_fields = ["cedula", "nombres", "apellidos"]

    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)



class AdminCuenta(admin.ModelAdmin):

    list_display = ["numero", "estado", "fechaApertura", "saldo", "tipoCuenta", "cliente"]
    list_filter = ["fechaApertura", "estado", "tipoCuenta"]
    search_fields = ["numero", "cliente"]

    class Meta:
        model = Cuenta

admin.site.register(Cuenta, AdminCuenta)

class AdminTransaccion(admin.ModelAdmin):

    list_display = ["transaccion_id","fecha", "tipo", "valor", "descripcion", "cuenta"]
    list_filter = ["tipo"]
    search_fields = ["cuenta", "descripcion"]

    class Meta:
        model = Transaccion

admin.site.register(Transaccion, AdminTransaccion)

class AdminTransferencia(admin.ModelAdmin):

    list_display = ["transferencia_id","fecha", "valor", "descripcion", "cuenta1", "cuenta2"]
    search_fields = ["cuenta1","cuenta2" "descripcion"]

    class Meta:
        model = Transferencia

admin.site.register(Transferencia, AdminTransferencia)


