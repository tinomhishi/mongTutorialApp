from django.core import serializers
from django.db import models
from django.utils import timezone


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def fetch_deleted(self):
        return super().get_queryset().filter(deleted_at__isnull=False)


class BaseModel(models.Model):
    deleted_at = models.DateTimeField(null=True, default=None)
    objects = BaseModelManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def to_json(self):
        return serializers.serialize('json', [self, ])

    class Meta:
        abstract = True
