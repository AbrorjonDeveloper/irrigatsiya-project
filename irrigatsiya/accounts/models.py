from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True, related_name="faculties")

    class Meta:
        unique_together = ('slug', 'parent', )
        verbose_name_plural = 'faculties'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Faculty, self).save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path = [self.name]
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Cafedra(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="cafedras")

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = 'cafedras'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Cafedra, self).save(*args, **kwargs)
    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path = [self.name]
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Level(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE, blank=True, null=True, related_name="level")

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = 'level'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Level, self).save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path = [self.name]
            k = k.parent
        return ' -> '.join(full_path[::-1])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="download.jpg", upload_to="avatar")
    faculty = models.ForeignKey('Faculty',on_delete=models.CASCADE, blank=True, null=True)
    cafedra = models.ForeignKey('Cafedra' ,on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey('Level' ,on_delete=models.CASCADE, blank=True, null=True)
    is_teacher = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width>300 or img.height>300:
            output = (300, 300)
            img.thumbnail(output)
            img.save(self.image.path)

    



