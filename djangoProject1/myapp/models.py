from django.db import models
from django.contrib.auth.model import User


class BlogPostCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        managed = True
        db_table = "blog_post_category"


class BlogPostTag(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        managed = True
        db_table = "blog_post_tag"

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogPostTag, blank=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = "blog_post"
