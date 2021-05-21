from django.contrib import admin
from projectmin.models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'owner')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'content', 'status')
