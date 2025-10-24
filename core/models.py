from django.conf import settings
from django.db import models


# Create your models here.
class Kit(models.Model):
    class Status(models.TextChoices):
        IN_USE = "in-use", "In Use"
        IN_TRANSIT = "in-transit", "In Transit"
        MAINTENANCE = "maintenance", "Maintenance"

    name = models.CharField(max_length=120)
    current_location = models.CharField(max_length=100, blank=True, default="")
    destination_location = models.CharField(max_length=100, blank=True, default="")
    issues = models.TextField(blank=True, null=True)
    needs_restock = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=Status, default='in_use')

    def __str__(self):
        return self.name


class PostMortem(models.Model):
    kit = models.ForeignKey(Kit, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=120)
    event_date = models.DateField()
    raw_text = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name





