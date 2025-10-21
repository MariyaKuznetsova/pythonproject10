from django.contrib import admin

from myblog.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "contents", "image", "is_publication", "number_of_views")
    list_filter = ("title",)
    search_fields = ("title", "contents")
