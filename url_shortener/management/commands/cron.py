import logging

from django.db.models.fields import return_None
from django.utils import timezone
from url_shortener.models import Link
from django.core.management.base import BaseCommand


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        deleted_count, _ = Link.objects.filter(deleted_at__lt=timezone.now()).delete()
        logger.info(f"Deleted {deleted_count} old links")
        return None
