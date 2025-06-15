from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name