from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','created',)
admin.site.register(Blog,BlogAdmin)
class CateAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category,CateAdmin,)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Tag,TagAdmin)