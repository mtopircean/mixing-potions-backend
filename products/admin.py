from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Product, Condition, BodySystem


class ConditionAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class BodySystemAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class ProductAdmin(ImportExportModelAdmin):
    search_fields = ('name', 'condition', 'body_systems',)
    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(BodySystem, BodySystemAdmin)
