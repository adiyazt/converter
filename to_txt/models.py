from django.db import models
import uuid

# Create your models here.

class WordFile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    filename = models.CharField(max_length=32, blank=False)