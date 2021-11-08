from django.db import models

class Wishes(models.Model):
    name = models.CharField(max_length=50)
    batch = models.BigIntegerField()
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.name
    