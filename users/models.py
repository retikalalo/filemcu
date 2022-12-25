from django.db import models

# membuat relasi antara tabel user bawaan django degan biodata yang dibuat
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Biodata(models.Model):
	#CASCADE berarti ketika user delete maka Biodatanya juga akan terhapus
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField()
	telp = models.CharField(max_length=16, blank=True, null=True)
	alamat = models.TextField(blank=True, null=True)

	def __str__(self):
		return "{} - {}".format(self.user, self.email)

	# agar pemulisan didashboard admin tidak ada penambahan s seperti bidatas
	class Meta:
		verbose_name_plural ="Biodata"
