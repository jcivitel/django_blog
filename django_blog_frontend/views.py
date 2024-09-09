from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from markdown import markdown

from django_blog_backend.models import BlogSettings, BlogPost


def dashboard(request):
    template = loader.get_template("dashboard.html")
    template_opts = dict()

    blog = BlogSettings.objects.first()

    if blog is None:
        return HttpResponseRedirect(reverse("setup"))

    template_opts["blog_title"] = blog.title
    template_opts["blog_description"] = markdown(blog.description)

    latest_post = BlogPost.objects.last()
    if latest_post is not None:
        latest_post.content = markdown(latest_post.content)
        template_opts["latest_post"] = latest_post
    messages.success(request, f"WELCOME ❤️")

    return HttpResponse(template.render(template_opts, request))


def post(request, post_id):
    template = loader.get_template("post.html")
    template_opts = dict()
    post = BlogPost.objects.get(pk=post_id)
    post.content = markdown(post.content)
    template_opts["post"] = post

    return HttpResponse(template.render(template_opts, request))
