from django.urls import path, include


urlpatterns = [
    #    path('admin/', admin.site.urls),
        path("", include("url_shortener.urls")),
]
