from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Experience._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.Education)
class DegreeAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Education._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Skill._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.About._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Reference._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Template._meta.fields if field.name not in ["created_at", "id"]
    ]


@admin.register(models.CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.CurriculumVitae._meta.fields if field.name not in ["created_at", "id"]
    ]
    filter_horizontal = ("skills", "experiences", "educations", "references")


@admin.register(models.UserDemographic)
class UserDemographicAdmin(admin.ModelAdmin):
    list_display = ['status', 'profession', 'user__email']
    # Make inline for socials
    search_fields = [
        'user__username', 'user__first_name', 'user__last_name', 'status'
    ]
