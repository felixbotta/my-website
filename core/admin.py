from django.contrib import admin

from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'description']

admin.site.register(Skill, SkillAdmin)

