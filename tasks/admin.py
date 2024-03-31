from django.contrib import admin
from django.db.models import Case, When, IntegerField

from .models import Task


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "due_date", "priority", "user", "complete")
    list_filter = ("creation_date", "due_date", "priority", "complete")
    search_fields = ("title",)
    ordering = (
        Case(
            When(priority="High", then=1),
            When(priority="Medium", then=2),
            When(priority="Low", then=3),
            default=4,
            output_field=IntegerField(),
        ),
    )


admin.site.site_header = "Task Manager Admin"
admin.site.site_title = "Task Manager Admin"
admin.site.index_title = "Task Manager Admin"

admin.site.register(Task, TaskAdmin)
