from django.contrib import admin
from .models import Biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
	#untuk membuat tabel yang rapi pada tabel dashboard
	list_display = ('user', 'email', 'telp', 'alamat')

	#untuk search data pada tabel dashboard admin
	search_fields = ('user', 'email')

admin.site.register(Biodata, BiodataAdmin)
