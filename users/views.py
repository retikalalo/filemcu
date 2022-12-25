from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def list_users(request):
	template_name = "users.html"
	context = {
		'title' : 'list_users',
	}
	return render(request, template_name, context)