from django.contrib import admin
from unit.models import Symbol, Unit, System


class SymbolAdmin(admin.ModelAdmin):
	list_display = ('symbol', 'author', )
	ordering = ('symbol', )
	search_fields = ('symbol', )
	save_as = True


class UnitAdmin(admin.ModelAdmin):
	list_display = ('name', 'symbol', 'author', )
	ordering = ('name', )
	search_fields = ('name', 'symbol', )
	save_as = True


class SystemAdmin(admin.ModelAdmin):
	list_display = ('name', 'author', )
	ordering = ('name', )
	search_fields = ('name', )
	save_as = True


admin.site.register(Symbol, SymbolAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(System, SystemAdmin)
