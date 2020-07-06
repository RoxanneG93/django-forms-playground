from django.db import models

# Create your models here.
class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=100)

    def __str__(self):
        return self.name