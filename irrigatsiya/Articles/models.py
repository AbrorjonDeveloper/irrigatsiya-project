from django.db import models
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,default=name, unique=True)
    # parent = models.ForeignKey('self' , on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    class Meta:
        unique_together = ( 'slug',) #'slug',,'parent'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        # full_path = [self.name]
        # k = self.parent

        # while k is not None:
        #     full_path = [self.name]
        #     k = k.parent
        # return ' -> '.join(full_path[::-1])
        return self.name


class Articles(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="article_category")
    article = models.FileField(blank=True, upload_to="articles")
    link = models.URLField(blank=True)
    slug = models.SlugField(unique=True)  #, default=__name__
    pub_date = models.DateTimeField( auto_now_add=True)
    up_date = models.DateTimeField( auto_now=True)
 
    class Meta:
        verbose_name_plural = 'Articles'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('articles')


