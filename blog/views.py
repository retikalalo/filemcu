from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import * #klo artikelnya diganti menjadi * berarti semua yang ada di models.py diambil semua ditampilkan
import requests
from .forms import ArtikelForms
from django.core.files.storage import FileSystemStorage



#BAGIAN API
def sinkron_filem(request):
	# URL = "https://imdb-api.com/en/API/SearchAll/k_n2dibjf6/trending"
	URL = "https://api.themoviedb.org/3/search/multi?api_key=5307d835e0a491d873eab1266a2ea5b5&language=en-US&page=1&include_adult=false&query=danur"

	r = requests.get(url = URL)        
	data = r.json()["results"]    
    
	for d in data:
		print(d['title'])
		cek_filem = Filem.objects.filter(title=d['title'])
		if cek_filem.exists(): # ini untuk update
			print("film sudah ada")
			film = cek_filem.first()
			film.poster_path = d['poster_path']
			film.overview = d['overview']
			film.release_date = d['release_date']
			film.vote_average = d['vote_average']
			film.save()
		else: # untuk buat baru
			print("film belum ada")
			Filem.objects.create(
				title = d['title'],
				poster_path = d['poster_path'],
				overview = d['overview'],
				release_date = d['release_date'],
				vote_average = d['vote_average']
			)
	return redirect(filem)	
#END API

@login_required
def filem(request):
	template_name = "back/tabel_filem.html"
	filem = Filem.objects.all() 
	context = {  
		'title' : 'FILEMCU | Filem-API',
		'db' : 'TABEL FILEM API',
		'filem' :filem,
	}
	return render(request, template_name, context)

#END API


@login_required
def dashboard(request):
	template_name = "back/dashboard.html"
	context = {
		'title' : 'FILEMCU | Dashboard',
		'db' : 'DASHBOARD'
	}
	return render(request, template_name, context)

@login_required
def artikel(request):
	template_name = "back/tabel_artikel.html"
	artikel = Artikel.objects.filter(nama = request.user)
	context = {  #ini format dictionary
		'title' : 'FILEMCU | TabelArtikel',
		'db' : 'TABEL ARTIKEL',
		'artikel' :artikel, #jarak diperhatikan
	}
	return render(request, template_name, context)

@login_required
def tambah_artikel(request):
	template_name = "back/tambah_artikel.html"
	kategory = Kategori.objects.all()

	if request.method == "POST":
		forms_artikel = ArtikelForms(request.POST, request.FILES)
		if forms_artikel.is_valid():
			art = forms_artikel.save(commit=False)
			art.nama = request.user
			art.save()
			return redirect(artikel)
	else:
		forms_artikel = ArtikelForms()

	context = {
		'title' : 'FILEMCU | TambahArtikel',
		'db' : 'ADD NEWS',
		'kategory' :kategory,
		'forms_artikel' :forms_artikel,
	}
	return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
	template_name = "back/lihat_artikel.html"
	artikel = Artikel.objects.get(id=id)
	context = {
		'title' : 'FILEMCU | LihatArtikel',
		'db' : 'LIHAT ARTIKEL',
		'artikel' : artikel,
	}
	return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
	template_name = "back/tambah_artikel.html"
	a = Artikel.objects.get(id=id)
	if request.method == "POST":
		forms_artikel = ArtikelForms(request.POST, instance=a)
		if forms_artikel.is_valid():
			art = forms_artikel.save(commit=False)
			art.nama = request.user
			art.save()
			return redirect(artikel)
	else:
		forms_artikel = ArtikelForms(instance=a)

	context = {
		'title' : 'FILEMCU | EditArtikel',
		'db' : 'EDIT ARTIKEL',
		'artikel' : a,
		'forms_artikel' :forms_artikel,
	}
	return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
	Artikel.objects.get(id=id).delete()
	return redirect(artikel)


@login_required
def users(request):
	template_name = "back/tabel_users.html"
	context = {
		'title' : 'FILEMCU | TabelUsers',
		'db' : 'TABEL USER'
	}
	return render(request, template_name, context)

