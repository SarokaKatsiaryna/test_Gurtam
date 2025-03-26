import logging
from django.contrib import admin
from django.contrib import messages
from django.utils import timezone
from url_shortener.models import Link, LinksGroup


logger = logging.getLogger(__name__)


@admin.action(description="Delete old links")
def delete_old_links(modeladmin, request, queryset):
    """Deleting old links."""
    deleted_count, _ = Link.objects.filter(deleted_at__lt=timezone.now()).delete()
    logger.info(f"Deleted {deleted_count} old links")
    messages.success(request, f"Deleted {deleted_count} old links.")

@admin.action(description="Delete link from group")
def delete_group_in_links(modeladmin, request, queryset):
    """Deleting selected links from groups."""
    links = list(queryset.values_list("long_url", "group"))
    count = queryset.update(group=None)
    for long_url, old_group in links:
        logger.info(f"Link URL={long_url} removed from group {old_group}")
    messages.success(request, f"Delete {count} links from group.")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "long_url", "short_url", "group", "deleted_at"]
    list_filter = ("group", "deleted_at")
    list_editable = ("long_url", "group")
    search_fields = ("long_url", "group__name")
    actions = [delete_group_in_links, delete_old_links]


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1
    fields = ("long_url", "short_url", "deleted_at", "group")


@admin.register(LinksGroup)
class LinksGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    inlines = [
        LinkInline,
    ]
