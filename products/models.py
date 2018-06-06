import random
import os
from django.db import models

def get_filename_ext(filepath):
     base_name = os.path.basename(filepath)
     name, ext = os.path.splitext(base_name)
     return name,ext

# Create your models here.
def upload_image_path(instance, filename):
    #print(instance)
    #print(filename)
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    file_file_name = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{ext}".format(
                                                    new_filename=new_filename,
                                                    final_filename=final_filename
                                                 )

class ProductQuerySet(models.query.QuerySet):
    def activate(self):
        return self.filter(featured=True, activate=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().featured()

    def featured(self): #product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None



class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    activate = models.BooleanField(default=True)

    objects = ProductManager()
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


