from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','show_genre')


    def show_genre(self,obj):
        html = '<ul>'
        for i in obj.genre.all():
            html += f'<li>{i}</li>'
        html += '</ul>'
        return mark_safe(html)


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title',)

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)