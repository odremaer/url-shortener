from hashlib import md5

from django.db import models



class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]


        # validate = URLValidator()
        # print(self.url_hash)
        # try:
        #     validate(self.full_url)
        # except ValidationError as e:
        #     raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)


