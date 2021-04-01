from django.contrib import admin
from .models import Articles, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    # pass
class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin)

admin.site.register(Articles, ArticlesAdmin)
