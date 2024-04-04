from django.db import models

from django.utils.text import slugify


# Create your models here.


class PostModel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField()
    category = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.judul)
        super(PostModel, self).save(force_insert,
                                    force_update, using, update_fields)

    def __str__(self):
        return '{}.{}'.format(self.id, self.judul)
