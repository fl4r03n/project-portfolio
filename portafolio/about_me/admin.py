from django.contrib import admin

from .models import Education, Experience, Skill, AboutMe, Knowledge, PortfolioHeader

@admin.register(PortfolioHeader)
class PortfolioHeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not PortfolioHeader.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False

@admin.register(Education)
class AboutMeEducation(admin.ModelAdmin):
    pass  # Dejar la clase vacía si no se necesitan campos de solo lectura

@admin.register(Experience)
class AboutMeExperience(admin.ModelAdmin):
    pass  # Dejar la clase vacía si no se necesitan campos de solo lectura

@admin.register(Skill)
class AboutMeSkill(admin.ModelAdmin):
    pass  # Dejar la clase vacía si no se necesitan campos de solo lectura

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Agregar campos de solo lectura
    
@admin.register(Knowledge)
class AboutMeKnowledge(admin.ModelAdmin):
    pass  # Dejar la clase vacía si no se necesitan campos de solo lectura