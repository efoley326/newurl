from django.db import models
from .utils import create_random_url

# Create your models here.
class Shortener(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=7, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_random_url()
        super().save(*args, **kwargs)