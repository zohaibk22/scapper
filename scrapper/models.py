from django.db import models

# Create your models here.
class Link(models.Model):
    address = models.CharField(max_length=2048, null=True, blank=True, unique=True)
    name = models.CharField(max_length=2048, null=True, blank=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return f"{self.name} ({self.address})"