from django.contrib import admin
from aplicacion.models import camion, objeto, ruta

class CamionAdmin(admin.ModelAdmin):
	list_display = ['nombreC']
class ObjetoAdmin(admin.ModelAdmin):
	list_display = ['nombreO']
class RutaAdmin(admin.ModelAdmin):
	list_display = ('camion','objeto')

# Register your models here.
admin.site.register(camion,CamionAdmin)
admin.site.register(objeto,ObjetoAdmin)
admin.site.register(ruta,RutaAdmin)
