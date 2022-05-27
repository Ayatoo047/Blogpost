from django.db import models
from django.contrib.auth.models import User


# class Title(models.Model):
#     name = models.CharField(max_length=70)

class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    snippet = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

# class Room(models.Model):
#     title = models.CharField(max_length=50)
#     room = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     created = models.DateField(auto_now=True)

