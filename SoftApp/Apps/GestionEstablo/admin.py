from django.contrib import admin
from SoftApp.Apps.GestionEstablo.models import *
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
 	list_display = [ "Nombre", "APaterno", "AMaterno", "FechaNacimiento" ]
 	search_fields =["Nombre"]
 	class Meta:
 		model = Empleado

class ContratoAdmin(admin.ModelAdmin):
 	list_display = [ "Empleado", "FechaInicio", "Paga", "Estado"]
 	search_fields =["Empleado__Nombre"]
 	class Meta:
 		model = Contrato

class VeladorAdmin(admin.ModelAdmin):
 	list_display = [ "Empleado", "FechaInicio","Estado"]
 	search_fields =["Empleado__Nombre"]
 	class Meta:
 		model = Veladore

class AreaAdmin(admin.ModelAdmin):
 	list_display = [ "Area", "Medidad","Estado"]
 	search_fields =["Medidad"]
 	class Meta:
 		model = Area

class CorraleAdmin(admin.ModelAdmin):
	list_display =["Capacidad", "Estado"]
	search_fields= ["Capacidad"]
	class Meta:
		model = Corrale

class AlmaceneAdmin(admin.ModelAdmin):
	list_display =["Empleado","Uso","Capacidad", "Estado"]
	search_fields= ["Uso"]
	class Meta:
		model = Almacene

class ProveedoreAdmin(admin.ModelAdmin):
	list_display =["Nombre","RFC","Telefono","Correo", "Estado"]
	search_fields= ["Nombre"]
	class Meta:
		model = Proveedore

class AnimaleAdmin(admin.ModelAdmin):
	list_display =["nombre","Codigo","Tipo"
									 "","Clasificacion"]
	search_fields= ["nombre"]
	class Meta:
		model = Animale

class AsignacionCorraleAdmin(admin.ModelAdmin):
	list_display =["Animal","Corral","FRegistro","Estado"]
	search_fields= ["Animal__nombre"]
	class Meta:
		model = AsignacionCorrale

class EstablonCorraleAdmin(admin.ModelAdmin):
	list_display =["Nombre","dueño","Numerotelefono","Correo","Estado"]
	search_fields= ["Animal__nombre"]
	class Meta:
		model = Establo

admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Contrato,ContratoAdmin)
admin.site.register(Veladore,VeladorAdmin)
admin.site.register(Area,AreaAdmin)
admin.site.register(Corrale,CorraleAdmin)
admin.site.register(Almacene,AlmaceneAdmin)
admin.site.register(Proveedore,ProveedoreAdmin)
admin.site.register(Animale,AnimaleAdmin)
admin.site.register(AsignacionCorrale,AsignacionCorraleAdmin)
admin.site.register(Establo,EstablonCorraleAdmin)

admin.site.site_header ="Establo Johan"


