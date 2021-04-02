from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Books(models.Model):
    name = models.CharField(max_length=300)
    book = models.FileField(blank=True, upload_to='Books')
    link = models.URLField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Books'

    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Books, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books")
    

