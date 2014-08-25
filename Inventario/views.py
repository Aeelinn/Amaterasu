from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
# , MaterialForm, EdificioForm, AulaForm, TipoForm, MarcaForm
from Inventario.forms import LoginForm
from Inventario.models import Material, Edificio, Aula, Tipo, Marca
from Tsukuyomi.settings import PAGINATION_ITEMS


# Vistas de material
class ListarMaterial(ListView):
    context_object_name = 'materiales'
    model = Material
    paginate_by = PAGINATION_ITEMS
    template_name = 'Inventario/materiales/listar_material.html'


class EliminarMaterial(DeleteView):
    context_object_name = 'material'
    model = Material
    success_url = reverse_lazy('Inventario:buscar_material')
    template_name = 'Inventario/materiales/eliminar_material.html'


class AgregarMaterial(CreateView):
    context_object_name = 'form'
    # form_class = MaterialForm
    model = Material
    success_url = reverse_lazy('Inventario:buscar_material')
    template_name = 'Inventario/materiales/agregar_material.html'


class ModificarMaterial(UpdateView):
    context_object_name = 'form'
    # form_class = MaterialForm
    model = Material
    success_url = reverse_lazy('Inventario:buscar_material')
    template_name = 'Inventario/materiales/modificar_material.html'


# Vistas de edificios
class ListarEdificios(ListView):
    context_object_name = 'edificios_query'
    model = Edificio
    paginate_by = PAGINATION_ITEMS
    template_name = 'Inventario/edificios/listar_edificios.html'


class EliminarEdificio(DeleteView):
    context_object_name = 'edificio'
    model = Edificio
    success_url = reverse_lazy('Inventario:listar_edificios')
    template_name = 'Inventario/edificios/eliminar_edificio.html'


class AgregarEdificio(CreateView):
    context_object_name = 'form'
    # form_class = EdificioForm
    model = Edificio
    success_url = reverse_lazy('Inventario:listar_edificios')
    template_name = 'Inventario/edificios/agregar_edificio.html'


class ModificarEdificio(UpdateView):
    context_object_name = 'form'
    # form_class = EdificioForm
    model = Edificio
    success_url = reverse_lazy('Inventario:listar_edificios')
    template_name = 'Inventario/edificios/modificar_edificio.html'


# Vistas aulas
class ListarAulas(ListView):
    context_object_name = 'aulas'
    model = Aula
    paginate_by = PAGINATION_ITEMS
    template_name = 'Inventario/aulas/listar_aulas.html'


class AgregarAula(CreateView):
    context_object_name = 'form'
    # form_class = AulaForm
    model = Aula
    success_url = reverse_lazy('Inventario:listar_aulas')
    template_name = 'Inventario/aulas/agregar_aula.html'


class ModificarAula(UpdateView):
    context_object_name = 'form'
    # form_class = AulaForm
    model = Aula
    success_url = reverse_lazy('Inventario:listar_aulas')
    template_name = 'Inventario/aulas/modificar_aula.html'


class EliminarAula(DeleteView):
    context_object_name = 'aula'
    model = Aula
    success_url = reverse_lazy('Inventario:listar_aulas')
    template_name = 'Inventario/aulas/eliminar_aula.html'


# Vistas tipos
class ListarTipos(ListView):
    context_object_name = 'tipos'
    model = Tipo
    paginate_by = PAGINATION_ITEMS
    template_name = 'Inventario/tipos/listar_tipos.html'


class AgregarTipo(CreateView):
    context_object_name = 'tipo'
    # form_class = TipoForm
    model = Tipo
    success_url = reverse_lazy('Inventario:listar_tipos')
    template_name = 'Inventario/tipos/agregar_tipo.html'


class ModificarTipo(UpdateView):
    context_object_name = 'tipo'
    # form_class = TipoForm
    model = Tipo
    success_url = reverse_lazy('Inventario:listar_tipos')
    template_name = 'Inventario/tipos/modificar_tipo.html'


class EliminarTipo(DeleteView):
    context_object_name = 'tipo'
    model = Tipo
    success_url = reverse_lazy('Inventario:listar_tipos')
    template_name = 'Inventario/tipos/eliminar_tipo.html'


# Vistas materiales
class ListarMarcas(ListView):
    context_object_name = 'marcas'
    model = Marca
    paginate_by = PAGINATION_ITEMS
    template_name = 'Inventario/marcas/listar_marcas.html'


class AgregarMarca(CreateView):
    context_object_name = 'marca'
    # form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('Inventario:listar_marcas')
    template_name = 'Inventario/marcas/agregar_marca.html'


class ModificarMarca(UpdateView):
    context_object_name = 'form'
    # form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('Inventario:listar_marcas')
    template_name = 'Inventario/marcas/modificar_marca.html'


class EliminarMarca(DeleteView):
    context_object_name = 'marca'
    model = Marca
    success_url = reverse_lazy('Inventario:listar_marcas')
    template_name = 'Inventario/marcas/eliminar_marca.html'


# Filtros
@login_required()
def buscar_material(request):
    if request.method == 'POST':
        buscar = request.POST['buscar']

        if buscar:
            materiales = Material.objects.filter(
                Q(codigo_interno__icontains=buscar) |
                Q(codigo_utez__icontains=buscar) |
                Q(codigo_vendedor__icontains=buscar)
            )
        else:
            materiales = Material.objects.all()
    else:
        buscar = ''
        materiales = Material.objects.all()

    paginator = Paginator(materiales, PAGINATION_ITEMS)

    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False

    return render(request, 'Inventario/filtros/busqueda.html',
                  {'buscar': buscar,
                   'materiales': page_obj,
                   'page_obj': page_obj,
                   'is_paginated': is_paginated,
                   'paginator': paginator})


@login_required()
def obtener_material_edificio(request, fk_edificio):
    nombre = get_object_or_404(Edificio, pk=fk_edificio).nombre

    materiales = Material.objects.all().select_related()
    materiales = [material for material in materiales
                  if material.ubicacion.edificio.pk == int(fk_edificio)]

    paginator = Paginator(materiales, PAGINATION_ITEMS)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False

    return render(request, 'Inventario/filtros/filtro_edificio.html',
                  {'nombre_edificio': nombre,
                   'materiales': page_obj,
                   'page_obj': page_obj,
                   'is_paginated': is_paginated,
                   'paginator': paginator})


@login_required()
def obtener_material_tipo(request, fk_tipo):
    nombre = get_object_or_404(Tipo, pk=fk_tipo).nombre

    tipos = Material.objects.filter(tipo=fk_tipo)

    paginator = Paginator(tipos, PAGINATION_ITEMS)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False

    return render(request, 'Inventario/filtros/filtro_tipo.html',
                  {'nombre_tipo': nombre,
                   'materiales': page_obj,
                   'page_obj': page_obj,
                   'is_paginated': is_paginated,
                   'paginator': paginator})


@login_required()
def obtener_material_marca(request, fk_marca):
    nombre = get_object_or_404(Marca, pk=fk_marca).nombre

    marcas = Material.objects.filter(marca=fk_marca)

    paginator = Paginator(marcas, PAGINATION_ITEMS)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False

    return render(request, 'Inventario/filtros/filtro_marca.html',
                  {'nombre_marca': nombre,
                   'materiales': page_obj,
                   'page_obj': page_obj,
                   'is_paginated': is_paginated,
                   'paginator': paginator})


# Sesiones
def login_form(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return redirect('Inventario:buscar_material')

    return render(request, 'Sesiones/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Inventario:login_form')


def reporte_general_material(request):
    def material_iterator():
        """
        Generador para evitar el consumo exesivo de memoria debido a la
        cantidad de elementos en el inventario
        """
        for material in Material.objects.all():
            yield [
                material.codigo_interno,
                material.codigo_utez,
                material.codigo_vendedor,
                material.ubicacion,
                material.marca,
                material.tipo,
                material.cantidad,
            ]

    data = [(
                "Código interno",
                "Código UTEZ",
                "Código fabricante",
                "Ubicación",
                "Marca",
                "Tipo",
                "Cantidad",
            )]

    for material in material_iterator():
        data.append(material)

    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; filename="reporte material %s.pdf"' % date.today()

    doc = SimpleDocTemplate(response, pagesize=landscape(letter))

    # container for the 'Flowable' objects
    elements = []

    t = Table(data)

    style = [
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),

        # Color cabecera tabla
        ('INNERGRID', (0, 0), (-1, 0), 1, colors.white),

        # Color tabla
        ('INNERGRID', (0, 1), (-1, -1), 1, colors.black),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ]

    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(('BACKGROUND', (0, i), (-1, i), colors.aliceblue))
        else:
            style.append(('BACKGROUND', (0, i), (-1, i), colors.aquamarine))

    t.setStyle(TableStyle(style))

    elements.append(t)

    # write the document to disk
    doc.build(elements)

    return response
