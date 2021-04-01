from django.contrib import admin
from .models import Profile, Faculty, Cafedra,Level
class FacultyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class CafedraAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class LevelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Profile)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Cafedra, CafedraAdmin)
admin.site.register(Level, LevelAdmin)

