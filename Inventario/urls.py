from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from Inventario.views import EliminarMaterial, ListarEdificios, EliminarEdificio, ListarAulas, \
    AgregarAula, ModificarAula, EliminarAula, ListarTipos, AgregarTipo, ModificarTipo, EliminarTipo, \
    ListarMarcas, \
    ModificarMarca, AgregarMarca, EliminarMarca, AgregarMaterial, ModificarMaterial, \
    ModificarEdificio, AgregarEdificio, reporte_general_material

urlpatterns = patterns(
    'Inventario.views',

    # Sesiones
    url(r'^login/$', 'login_form', name='login_form'),
    url(r'^logout/$', 'user_logout', name='user_logout'),

    # Reporte PDF
    url(r'^reporte_general/$', 'reporte_general_material', name='reporte_material'),

    # CRUD de usuarios
    url(r'^edificios/$', login_required(ListarEdificios.as_view()), name='listar_usuarios'),
    url(r'^edificios/agregar/$', login_required(AgregarEdificio.as_view()), name='agregar_usuario'),
    url(r'^edificios/modificar/(?P<pk>\d+)/$', login_required(ModificarEdificio.as_view()),
        name='modificar_usuario'),
    url(r'^edificios/eliminar/(?P<pk>\d+)/$', login_required(EliminarEdificio.as_view()),
        name='eliminar_usuario'),

    # CRUD de materiales
    # url(r'^$', login_required(ListarMaterial.as_view()), name='listar_material'),
    url(r'^$', 'buscar_material', name='buscar_material'),
    url(r'^materiales/agregar/$', login_required(AgregarMaterial.as_view()),
        name='agregar_material'),
    url(r'^materiales/modificar/(?P<pk>\d+)/$', login_required(ModificarMaterial.as_view()),
        name='modificar_material'),
    url(r'^materiales/eliminar/(?P<pk>\d+)/$', login_required(EliminarMaterial.as_view()),
        name='eliminar_material'),

    # CRUD de edificios
    url(r'^edificios/$', login_required(ListarEdificios.as_view()), name='listar_edificios'),
    url(r'^edificios/agregar/$', login_required(AgregarEdificio.as_view()),
        name='agregar_edificio'),
    url(r'^edificios/modificar/(?P<pk>\d+)/$', login_required(ModificarEdificio.as_view()),
        name='modificar_edificio'),
    url(r'^edificios/eliminar/(?P<pk>\d+)/$', login_required(EliminarEdificio.as_view()),
        name='eliminar_edificio'),

    # CRUD de aulas
    url(r'^aulas/$', login_required(ListarAulas.as_view()), name='listar_aulas'),
    url(r'^aulas/agregar/$', login_required(AgregarAula.as_view()), name='agregar_aula'),
    url(r'^aulas/modificar/(?P<pk>\d+)/$', login_required(ModificarAula.as_view()),
        name='modificar_aula'),
    url(r'^aulas/eliminar/(?P<pk>\d+)/$', login_required(EliminarAula.as_view()),
        name='eliminar_aula'),

    # CRUD tipos de material
    url(r'^tipos/$', login_required(ListarTipos.as_view()), name='listar_tipos'),
    url(r'^tipos/agregar$', login_required(AgregarTipo.as_view()), name='agregar_tipo'),
    url(r'^tipos/modificar/(?P<pk>\d+)/$', login_required(ModificarTipo.as_view()),
        name='modificar_tipo'),
    url(r'^tipos/eliminar/(?P<pk>\d+)/$', login_required(EliminarTipo.as_view()),
        name='eliminar_tipo'),

    # CRUD de marcas
    url(r'^marcas/$', login_required(ListarMarcas.as_view()), name='listar_marcas'),
    url(r'^marcas/agregar/$', login_required(AgregarMarca.as_view()), name='agregar_marca'),
    url(r'^marcas/modificar/(?P<pk>\d+)/$', login_required(ModificarMarca.as_view()),
        name='modificar_marca'),
    url(r'^marcas/eliminar/(?P<pk>\d+)/$', login_required(EliminarMarca.as_view()),
        name='eliminar_marca'),

    # Filtros
    # url(r'^materiales/buscar/$', 'buscar_material', name='buscar_material'),
    url(r'^materiales/edificio/(?P<fk_edificio>\d+)/$', 'obtener_material_edificio',
        name='filtro_edificio'),
    url(r'^materiales/tipo/(?P<fk_tipo>\d+)/$', 'obtener_material_tipo', name='filtro_tipo'),
    url(r'^materiales/marca/(?P<fk_marca>\d+)/$', 'obtener_material_marca', name='filtro_marca'),
)