from django.contrib.auth.models import User
from django.db import models


class BlogSettings(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    default_language = models.CharField(
        max_length=2, default="en", help_text="Default language as CODE exam. 'en'"
    )
    social_media_links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField(help_text="Content of the post in Markdown")
    category = models.ForeignKey(BlogSettings, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(
        "PostImage", on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField("Tag", related_name="blog_posts")
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    image = models.ImageField(upload_to="blog_images")
    caption = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPostView(models.Model):
    blog_post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name="views"
    )
    viewer_ip = models.GenericIPAddressField()
    view_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.view_date} - {self.viewer_ip}"
