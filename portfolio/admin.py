from django.contrib import admin
from .models import BlogPost, Gallery, BlogImage

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Gallery)
admin.site.register(BlogImage)
