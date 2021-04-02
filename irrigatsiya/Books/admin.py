from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Books, BooksAdmin)

