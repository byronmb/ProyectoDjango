from django.db import models

# Create your models here.
"""
Modelo de Cliente que posee cuentas
"""
class Cliente(models.Model):

    listaGenero = (
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    )
    listaEstadoCivil = (
        ('soltero', 'Solter@'),
        ('casado', 'Casad@'),
        ('viudo', 'Viud@'),
        ('divorciado', 'Divorciad@'),
        ('unionLibre', 'Unión Libre'),
    )

    cliente_id = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10, null = False)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    genero = models.CharField(max_length=15, choices = listaGenero, default ='m', null = False)
    estadoCivil = models.CharField(max_length=15, choices = listaEstadoCivil, default ='soltero', null = False)
    fechaNacimiento = models.DateField(auto_now = False, auto_now_add = False, null = False)
    correo = models.EmailField(unique=True, max_length=100, null = False)
    telefono = models.CharField(max_length=10, null = False)
    celular = models.CharField(max_length=10, null = False)
    direccion = models.TextField(null = False)
    #uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.cedula

"""
Modelo de Cuenta que se relaciona con cliente
"""
class Cuenta(models.Model):

    listaTipo = (
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorro'),
        ('nomina', 'Nómina'),
        ('valores', 'Valores'),

    )
    cuenta_id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20, unique=True, null = False)
    estado = models.BooleanField(null = False, default = True)
    fechaApertura = models.DateField(auto_now_add = True, null = False)
    saldo = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    tipoCuenta = models.CharField(max_length=30, choices = listaTipo, default ='ahorros', null = False)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.numero
"""
Modelo de Transaccion, en una cuenta se realizan varias transacciones de todo tipo
estas tienen un responsable, que puede ser un/a cajer@, trnasferencia online
o uso del servicio de cajero automatico
"""
class Transaccion(models.Model):

    listaTipoC = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),

     )
    transaccion_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    tipo = models.CharField(max_length=30, choices = listaTipoC, default ='deposito', null = False)
    valor = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    descripcion = models.TextField(null = False)
    cuenta = models.ForeignKey(
        'Cuenta',
        on_delete=models.CASCADE,
    )

class Transferencia(models.Model):

    transferencia_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    valor = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    descripcion = models.TextField(null = False)
    cuenta1 = models.ForeignKey(
        'Cuenta',
        related_name='cuenta1',
        on_delete=models.CASCADE,
    )
    cuenta2 = models.ForeignKey(
        'Cuenta',
        related_name='cuenta2',
        on_delete=models.CASCADE,
    )




