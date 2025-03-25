from django.utils import timezone
from nanoid import generate
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import CreateView
from url_shortener.forms import LinkForm
from url_shortener.models import Link


class HomeView(CreateView):
    template_name = "home.html"
    form_class = LinkForm

    def post(self, request, *args, **kwargs):
        form = LinkForm(request.POST)
        try:
            long_url_request = request.POST.get("long_url")
            url_object = Link.objects.get(
                Q(long_url=f"http://{long_url_request}")
                | Q(long_url=f"https://{long_url_request}")
                | Q(long_url=long_url_request)
            )  # Checking the existence of the link in the database
        except Link.DoesNotExist:
            if form.is_valid():
                form_save = form.save(commit=False)
                short_url = generate(
                    size=4
                )  # It can generate more than 16_000_000 identifiers
                try:
                    while Link.objects.get(
                        short_url=short_url
                    ):  # Checking the existence of the short link in the database
                        short_url = generate(size=4)
                except Link.DoesNotExist:
                    form_save.short_url = short_url
                    form_save.save()
                    url_object = form_save
            else:
                return render(request, "home.html", {"form": form})
        context = {
            "form": LinkForm(),
            "long_url": url_object.long_url,
            "short_url": url_object.short_url,
        }
        return render(request, "home.html", context)


def redirect_view(request, slug):
    try:
        url_object = Link.objects.get(short_url=slug)
        url_object.used_at = timezone.now()  # Extending the link's lifetime
        url_object.save()
        return redirect(url_object.long_url)
    except Link.DoesNotExist:
        return render(request, "404.html")
