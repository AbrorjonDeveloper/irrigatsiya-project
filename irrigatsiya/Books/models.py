from django.db import models
from django.utils.text import slugify

class Books(models.Model):
    name = models.CharField(max_length=300)
    book = models.FileField(blank=True, upload_to='Books')
    link = models.URLField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Books'
    
    def save(self):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(Books, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
