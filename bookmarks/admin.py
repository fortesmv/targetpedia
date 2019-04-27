from django.contrib import admin
from .models import Bookmark, Tag

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username', 'tags')
    search_fields = ['url', 'title', 'description', 'tags']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag)