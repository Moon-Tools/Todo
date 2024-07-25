from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=255, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  isDone = models.BooleanField(default=False)
  