from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=20)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name="pedidos")
    id_empleado = models.IntegerField()  # Si no está relacionado con empleado aún
    fecha_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=30, choices=[
        ('Pendiente', 'Pendiente'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado')
    ])
    direccion = models.TextField()
    forma_pago = models.CharField(max_length=20, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta')
    ])

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.id_cliente.nombre} {self.id_cliente.apellido}"
