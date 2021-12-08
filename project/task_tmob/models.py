from django.db import models
from django.utils import timezone
from ..redis_conection import add_to_redis, delete_value_from_redis


class Redirect(models.Model):
    key = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        if not self.active:
            delete_value_from_redis(self.key)
        else:
            add_to_redis(key=self.key,
                       val=self.url)
        return super(Redirect, self).save(*args, **kwargs)