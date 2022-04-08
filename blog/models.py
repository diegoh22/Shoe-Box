from django.db import models
from jdango.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.model):
    title = models.CharField(max_length=200, unique=True)
    slug = models,SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    like = models.ManyToManyField(User, related_name='blog_like', blank=True)

    class Meta:
        ordering = ['-created_on']

    def _str_(self):
        return self.title 

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    


# Create your models here.
