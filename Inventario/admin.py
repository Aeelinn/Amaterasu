from django.contrib import admin
from Inventario.models import Material, Edificio, Aula, Marca, Tipo

# Register your models here.


class InventarioAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_interno', 'codigo_utez', 'codigo_vendedor',
        'marca', 'tipo'
    )
    # list_filter = ('codigo_interno', 'codigo_utez', 'codigo_vendedor')
    # list_per_page = 1
    search_fields = ('codigo_interno', 'codigo_utez', 'codigo_vendedor')


admin.site.register((Edificio, Aula, Marca, Tipo))
admin.site.register(Material, InventarioAdmin)
