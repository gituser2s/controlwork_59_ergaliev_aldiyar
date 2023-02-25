from django.contrib import admin
from webapp.models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'email', 'status', 'created_at')
    list_filter = ('id', 'author', 'text', 'email', 'status', 'created_at')
    search_fields = ('author', 'text', 'email', 'status')
    fields = ('author', 'text', 'email', 'status', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Book, BookAdmin)
