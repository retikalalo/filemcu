#dalam urls.py merupakan isi daam semua path


from django.contrib import admin
from django.urls import path, include



########### untuk media #############
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500

# memanggil fungsi home yang ada didalam file views
from . views import *


urlpatterns = [
    path("admin/", admin.site.urls), #klo path '', maksudnya hanya memanggil localhost\:8000 dan biasanya akan diberitahukan kali path belum ditemukan.
    #apps
    path("dashboard/", include('blog.urls')),
    path('users/',include('users.urls')),
    path('', index, name='index'),
    path('artikel-list/', artikel_list, name='artikel_list'),
    path('artikel-detail/<int:id>', artikel_detail, name='artikel_detail'),
    path('contact-us/', contact, name='contact'),
    # path('filem/detail/<str:key>', filem_detail, name='filem_detail'),

    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', search, name='search'),
    path('<int:movie_id>/', view_movie_detail, name='movie_detail'),
    
]

######## untuk media ##########
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)