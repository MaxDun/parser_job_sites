from django.contrib import admin
from .models import Job


@admin.register(Job)
class GroupConfigAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created_at', 'name', 'source', 'url', 'salary_info', 'place_info')
    list_filter = ('created_at', 'source')
