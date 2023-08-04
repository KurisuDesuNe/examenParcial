from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse 

# Create your views here.

listaProductos=[]   
listaTienda=[]

def index(request):
    return HttpResponse("Bienvenidos a Django")

def ejemplo(request):
    return HttpResponse("Bienvenido a un ejemplo")

def ejercicio(request):
    return HttpResponse("Bienvenido a un ejercicio")

def PanelTienda(request):
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        provincia = request.POST.get('provincia')
        region = request.POST.get('region')
        fechacrea = request.POST.get('fechacrea')
        telefono = request.POST.get('telefono')

        listaTienda.append([direccion,provincia,region,fechacrea,telefono]) 
            return HttpResponseRedirect(reverse('gestionTiendas:PanelTienda'))


    return render(request, 'PanelTienda.html',{
        'listaTienda':listaTienda,
    })

def Productos(request):
    print(request.POST)
    if request.method == 'POST':
        descproducto = request.POST.get('descproducto')
        codigo = request.POST.get('codigo')
        precioventa = request.POST.get('precioventa')
        cantidad = request.POST.get('cantidad')
        relacionada = request.POST.get('relacionada')

        listaProductos.append([descproducto,codigo,precioventa,cantidad,relacionada]) 
            return HttpResponseRedirect(reverse('gestionTiendas:PanelProductos'))
    
    return render(request, 'PanelProductos.html',{
        'listaProductos':listaProductos,
    })
