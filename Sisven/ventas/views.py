
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Producto, Categoria
from .form import ProductoForm  

# Listar productos
@login_required
@permission_required('ventas.view_producto', raise_exception=True)
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/productos.html', {'productos': productos})

# Crear producto
@login_required
@permission_required('ventas.add_producto', raise_exception=True)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'ventas/crear_producto.html', {'form': form})

# Ver detalle de un producto
@login_required
@permission_required('ventas.view_producto', raise_exception=True)
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'ventas/detalle_producto.html', {'producto': producto})

# Editar producto
@login_required
@permission_required('ventas.change_producto', raise_exception=True)
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/editar_producto.html', {'form': form})

# Eliminar producto
@login_required
@permission_required('ventas.delete_producto', raise_exception=True)
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'ventas/eliminar_producto.html', {'producto': producto})