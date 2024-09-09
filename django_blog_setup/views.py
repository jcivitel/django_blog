from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django_blog_backend.models import BlogSettings
from .forms import BlogSettingForm


def setup(request):
    if BlogSettings.objects.first() is not None:
        return HttpResponseRedirect(reverse("dashboard"))
    if request.method == "POST":
        settings_form = BlogSettingForm(request.POST)
        if settings_form.is_valid():
            BlogSettings.objects.create(
                title=settings_form.cleaned_data["title"],
                description=settings_form.cleaned_data["description"],
                default_language=settings_form.cleaned_data["default_language"],
            )
            last_user = User.objects.create(
                username=settings_form.cleaned_data["email"],
                email=settings_form.cleaned_data["email"],
                first_name=settings_form.cleaned_data["name"],
            )
            last_user.set_password(settings_form.cleaned_data["password"])
            last_user.save()
            return HttpResponseRedirect(reverse("dashboard"))
    template = loader.get_template("setup.html")
    template_opts = dict()
    template_opts["form"] = BlogSettingForm

    return HttpResponse(template.render(template_opts, request))
