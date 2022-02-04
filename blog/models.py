from tabnanny import verbose
from django.db import models
from django.db import models
#from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, verbose_name='Url', unique=True)
    author = models.CharField(max_length=64)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Последнее обновление')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank = True)
    views = models.IntegerField(default = 0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']





