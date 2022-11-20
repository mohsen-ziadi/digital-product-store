from django.db import models



class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    description = models.TextField('description', blank=True)
    avatar = models.ImageField('avatar', blank=True, upload_to='categories/')
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField('title',max_length=50)
    description = models.TextField('description', blank=True)
    avatar = models.ImageField('avatar', blank=True, upload_to='avatar/')
    is_enable = models.BooleanField('is enable', default=True)
    categories = models.ManyToManyField('Category', verbose_name='category')
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ('-created_time',)

    def __str__(self):
        return self.title

class File(models.Model):
    product = models.ForeignKey('Product',verbose_name='product',related_name='files',on_delete=models.CASCADE)
    title = models.CharField('title',max_length=50)
    file = models.FileField('file', upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField('is enable', default=True)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    updated_time = models.DateTimeField('updated time', auto_now=True)

    class Meta:
        db_table = 'files'
        ordering = ('-created_time',)

    def __str__(self):
        return self.title