from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField('Items', related_name='categories')


    def __str__(self):
        return self.name


class Items(models.Model):
    icon = models.FileField(upload_to='media')
    name = models.CharField(max_length=50)
    onclick_func = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name