import logging
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


logger = logging.getLogger(__name__)


class LinksGroup(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Name of group")

    def __str__(self):
        return self.name


class Link(models.Model):
    short_url = models.CharField(max_length=10, unique=True)
    long_url = models.URLField(unique=True)
    created_at = models.DateTimeField(null=True, blank=True)
    time_to_live = models.PositiveIntegerField(
        default=180,
        validators=[MinValueValidator(1), MaxValueValidator(366)]
    )
    deleted_at = models.DateTimeField(null=True, blank=True)
    group = models.ForeignKey(
        LinksGroup, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return self.long_url

@receiver(pre_save, sender=Link)
def log_link_changes(sender, instance, **kwargs):
    if instance.created_at is None:
        instance.created_at = timezone.now()
    if instance.deleted_at is None:
        instance.deleted_at = instance.created_at + timedelta(days=int(instance.time_to_live))
    if instance.pk is None:
        logger.info(f"Created new link: URL={instance.long_url}: {instance.short_url}")
    else:
        logger.info(f"Updated link: URL={instance.long_url}: {instance.short_url}")


@receiver(pre_save, sender=LinksGroup)
def log_link_group_changes(sender, instance, **kwargs):
    if instance.pk is None:
        logger.info(f"Created new link group: name={instance.name}")
    else:
        logger.info(f"Updated link group: name={instance.name}")


@receiver(pre_delete, sender=Link)
def log_link_deletion(sender, instance, **kwargs):
    logger.info(f"Link deleted: URL={instance.long_url}: {instance.short_url}")


@receiver(pre_delete, sender=LinksGroup)
def log_link_group_deletion(sender, instance, **kwargs):
    logger.info(f"Link group deleted: name={instance.name}")
