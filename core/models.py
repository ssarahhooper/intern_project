from django.conf import settings
from django.db import models


# Create your models here.
class Kit(models.Model):

    name = models.CharField(max_length=120)
    current_location = models.CharField(max_length=100, blank=True, default="")
    destination_location = models.CharField(max_length=100, blank=True, default="")
    issues = models.TextField(blank=True, null=True)
    needs_restock = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostMortem(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)
    event_name = models.CharField(max_length=120)
    event_date = models.DateField()
    summary = models.TextField()
    issues = models.TextField(blank=True, null=True)
    restock = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name





