from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    save_as = True
    list_display = ('id','title','slug','category','created_at','updated_at', 'get_photo', 'views')
    list_display_links =('id','title')
    search_field =('title')
    list_filter = ('category', 'tags')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width = "50">')
        return '-'

    get_photo.short_description = 'Фото'

   
