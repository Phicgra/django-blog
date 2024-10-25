from django.db import models
from datetime import datetime

# Create your models here.

class Blog_post(models.Model):
    author = models.CharField(max_length=255, default="Your name here")
    title = models.CharField(max_length=255,default="Title of your Post")
    blog_content = models.TextField(max_length=10000, default="Your of your Post")

    time = models.DateTimeField(auto_now_add=True)

