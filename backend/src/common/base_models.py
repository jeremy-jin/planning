from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
