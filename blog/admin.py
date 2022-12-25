from django.contrib import admin
from .models import *

class ArtikelAdmin(admin.ModelAdmin):
	list_display = ('nama', 'judul', 'body', 'kategory', 'date', 'img', 'published')

class FilemAdmin(admin.ModelAdmin):
	list_display = ('title', 'poster_path', 'overview', 'release_date', 'vote_average')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(Filem, FilemAdmin)
admin.site.register(Comment)

