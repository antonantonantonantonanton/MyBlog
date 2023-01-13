from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """Posts"""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """It returns row representation."""
        return self.title

