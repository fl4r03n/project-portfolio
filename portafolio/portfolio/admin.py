from django.contrib import admin
from .models import Project
# Register your models here.

@admin.register(Project) #equivale a admin.site.register(Project) nesesario para ver los campos created y updated
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
