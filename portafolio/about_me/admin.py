from django.contrib import admin

from .models import Education, Experience, Skill, SkillDesc, AboutMe, PortfolioHeader, Fact, FactDesc, ResumeDesc

@admin.register(PortfolioHeader)
class PortfolioHeaderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not PortfolioHeader.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "start_year", "end_year")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_year", "end_year")

@admin.register(SkillDesc)
class SkillDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not SkillDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False
    
@admin.register(ResumeDesc)
class ResumeDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not ResumeDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name","skill_type", "percentage")

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")  # Agregar campos de solo lectura
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not AboutMe.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False
    

@admin.register(FactDesc)
class FactDescAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existe una instancia
        return not FactDesc.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ("title", "end_value", "duration")

    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar si ya existen 4 registros
        if Fact.objects.count() >= 4:
            return False
        return True