from django.contrib import admin
from django.urls import path, include, re_path

import django_blog_frontend.views

urlpatterns = [
    re_path(r"^$", django_blog_frontend.views.dashboard),
    path("admin/", admin.site.urls),
    path("blog/", include("django_blog_frontend.urls")),
    path("setup/", include("django_blog_setup.urls")),
]
