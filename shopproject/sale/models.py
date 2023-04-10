from django.db import models

# Create your models here.

from django.urls import reverse


# Create your models here.
class Category (models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('sale:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)
class Product(models.Model):

    category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name=models.CharField(max_length=200, db_index=True)
    slug=models.SlugField(max_length=200, db_index=True)
    image=models.ImageField(upload_to='products', blank=True)
    stock=models.IntegerField()
    desc=models.CharField(max_length=300, default='')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def get_url(self):return reverse('sale:prodCatdetail', args=[self.category.slug,self.slug])



    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)


