from hashlib import md5

from django.db import models


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)


