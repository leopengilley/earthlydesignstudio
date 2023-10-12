from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length = 70)
    date = models.DateField(auto_now = True)
    body = models.TextField(max_length = 1000)
    images = models.ManyToManyField('BlogImage', blank=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField()
    description = models.CharField(max_length = 250, blank=True)

    def __str__(self):
        return self.title


class BlogImage(models.Model):
    blogPost = models.ForeignKey('BlogPost', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField()
