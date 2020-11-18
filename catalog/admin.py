from django.contrib import admin
from .models import Catalog, Service


class AdminCatalog(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Catalog, AdminCatalog)


class AdminService(admin.ModelAdmin):
    list_display = ['name', 'gender', 'slug', 'price_1', 'price_2', 'price_3', 'price_4', 'price_nm_1', 'price_nm_2', 'price_nm_3',
                    'price_nm_4', 'price_man', 'price_man_material', 'price_man_all']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['id', 'catalog', ]
    list_editable = ('gender',)



admin.site.register(Service, AdminService)
