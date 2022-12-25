#dalam views.py merupakan semua fungsi

from django.shortcuts import render, redirect, get_object_or_404 #untuk memanggil file html
from django.http import HttpResponse #formasi html langsung ditulis didalam HttpReasponse

from django.contrib.auth import authenticate #lib authenticate itu untuk mengecek ke database
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

from blog.models import *
import requests
from blog.forms import CommentForm



TMDB_API_KEY = '5307d835e0a491d873eab1266a2ea5b5'

def search(request):

    # Get the query from the search box
    query = request.GET.get('q')
    print(query)

    # If the query is not empty
    if query:

        # Get the results from the API

        data = requests.get(f"https://api.themoviedb.org/3/search/multi?api_key={TMDB_API_KEY}&language=en-US&page=1&include_adult=false&query={query}")
        print(data.json())

    else:
        return HttpResponse("Please enter a search query")

    # Render the template
    return render(request, 'front/results.html', {
        "data": data.json(),
        "type": request.GET.get("type"),
		'title' : 'FILEMCU - RESULTS',
    })

def view_movie_detail(request, movie_id):
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US")
    return render(request, "front/movie_detail.html", {
        "data": data.json(),
        "type": "movie",
		'title' : 'FILEMCU - RESULTS',
    })

# #API END


def index(request):
	template_name = 'front/index.html'
	film = Filem.objects.all()
	if request.method  == "POST":
		search = request.POST.get("judul")
		search_film = Filem.objects.filter(title__icontains=search)
		print(search_film)
		
	search_film = []
	context = {
		'title' : 'FILEMCU',
		'welcome' : 'welcome my home',
		'film' : film,
		'search_film' : search_film,
	}
	return render(request, template_name, context)

def artikel_list(request):
	template_name = "front/artikel_list.html"
	artikel = Artikel.objects.filter(published=True)
	context = {  
		'title' : 'FILEMCU | ARTIKEL LIST', 
		'artikel' :artikel,

	}
	return render(request, template_name, context)


def contact(request):
	template_name = "front/contact.html"
	context = {  
		'title' : 'FILEMCU | ABOUT ME', 
	}
	return render(request, template_name, context)


def artikel_detail(request, id):
	template_name = "front/artikel_detail.html"
	artikel = Artikel.objects.get(id=id)

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.artikel = artikel
			obj.save()
		return redirect(artikel_detail, id=artikel.id)
	else:
		form = CommentForm()

	context = {  
		'title' : 'FILEMCU | ARTIKEL DETAIL', 
		'form' :form,
		'artikel' :artikel,
	}
	return render(request, template_name, context)


def login(request):
	if request.user.is_authenticated:
		print('sudah login')
		redirect('index')
		
	template_name = "akun/login.html"
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username, password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			#data ada
			print('username benar')
			auth_login(request, user)
			return redirect('index')
		else:
			#data tidak ada
			print('username salah')
	context = {  
		'title' : 'FILEMCU | FORM LOGIN', 
	}
	return render(request, template_name, context)


def logout_view(request):
	logout(request)
	return redirect('index')


# def artikel_detail(request, id):
# 	template_name = "front/artikel_detail.html"
# 	artikel = Artikel.objects.get(id=id)
# 	print(artikel)
# 	context = {  
# 		'title' : 'FILEMCU | ARTIKEL DETAIL', 
# 		'artikel' :artikel,
# 	}
# 	return render(request, template_name, context)
