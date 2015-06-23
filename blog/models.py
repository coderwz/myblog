from django.db import models
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank = True, null = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Author(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.username
