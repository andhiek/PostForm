from django.db import models

# Create your models here.


class ContactModel(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    alamat = models.TextField()

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)
