from django.contrib import admin
from source.models import Origin, Source


class OriginAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', )
	ordering = ('name', )
	search_fields = ('name', )
	save_as = True


class SourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'origin', 'url', )
	ordering = ('name', )
	search_fields = ('name', 'origin', )
	save_as = True


admin.site.register(Source, SourceAdmin)
admin.site.register(Origin, OriginAdmin)
