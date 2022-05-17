from django.db import models
from django.shortcuts import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=40)
    price = models.FloatField(max_length=20)
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
