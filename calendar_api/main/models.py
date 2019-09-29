from django.db import models
from django.utils import timezone
from django.urls import reverse

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_finished = models.DateTimeField(db_index=True, null=True)
    def save(self, *args, **kwargs):
        self.event_finished = timezone.now()
        return super().save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("event_detail_view", args=[str(self.id)])
    def __str__(self):
        return self.event_name
    class Meta:
        ordering = ["-event_finished"]
