from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Pedido, Empleado
from .forms import ClienteForm, PedidoForm, EmpleadoForm

# Página de inicio
def inicio_mcdonalds(request):
    return render(request, 'inicio_mcdonalds.html')

# ======== CLIENTES ========
def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_cliente.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_cliente')
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ver_cliente')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/actualizar_cliente.html', {'form': form})

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})


# ======== PEDIDOS ========
def ver_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/ver_pedido.html', {'pedidos': pedidos})

def agregar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_pedido')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/agregar_pedido.html', {'form': form})

def actualizar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('ver_pedido')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/actualizar_pedido.html', {'form': form})

def borrar_pedido(request, id_pedido):
    pedido = get_object_or_404(Pedido, id_pedido=id_pedido)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido')
    return render(request, 'pedidos/borrar_pedido.html', {'pedido': pedido})


# ======== EMPLEADOS ========
def ver_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleado.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})

def actualizar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('ver_empleado')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/actualizar_empleado.html', {'form': form})

def borrar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleado')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})
