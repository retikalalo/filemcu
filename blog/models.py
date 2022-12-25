from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


# # Create your models here.
class Kategori(models.Model):
	nama = models.CharField(max_length=20)

	def __str__(self): #fungsi ini berguna untuk ketika dipanggil maka akan mengembalikan nama
		return self.nama #self merujuk ke class, maka akan mengambil data yang ada di dalam kelas
		#pada return jika tidak menggunakan kata self maka akan mencari nama yang ada di luar kelas, bukan didalamnya.

	class Meta:
		verbose_name_plural = "Kategori"		

class Artikel(models.Model):
	#max_length berguna untuk panjang namanya berapa. blank false karena data tidak akan bisa di create tanpa diisi nama
	nama = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
	# nama = models.CharField(max_length=100, blank=True, null=True)
	judul = models.CharField(max_length=100)
	body = models.TextField()
	kategory = models.ForeignKey(Kategori, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	img = models.FileField(upload_to='img', blank=True, null=True)
	published = models.BooleanField(default=True)


	def __str__(self):
		return "{} - {}".format(self.nama, self.judul) #ini jika kita akan mengambil 2 variabel yang ada di dalam kelas

	class Meta:
		ordering = ['-date'] #mengambil id dari yang terbesar dahulu baru terkecil, klo diganti judul juga dari huruf terbesar
		verbose_name_plural = "Artikel"
		

class Filem(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	poster_path = models.ImageField(blank=True, null=True)
	overview = models.TextField(blank=True, null=True)
	release_date = models.CharField(max_length=100)
	vote_average = models.CharField(max_length=100)

	def __str__(self):
		return self.title 

	class Meta:
		verbose_name_plural = "Filem"


class Comment(models.Model):
    artikel = models.ForeignKey(Artikel,on_delete=models.CASCADE,related_name='comments')
    nama = models.CharField(max_length=80)
    # email = models.EmailField()
    komen = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.artikel.judul, self.nama)
		
# 	#selesai membuat database yang akan dibuat, pada cmd harus selalu di migrate
# 	#setiap ada perubahan pada database yang dibuat wajib di migrate
# 	#migrate samadengan dengan eksekusi biar bisa masuk ke database
# 	#di django primary key nya id, selalu ada tapi disembunyikan