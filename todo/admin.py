from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_completed',)
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'content')
