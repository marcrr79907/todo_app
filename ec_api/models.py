from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField()
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]

    class Meta:
        ordering = ['-updated']
