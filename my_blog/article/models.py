# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length = 128)
    category = models.CharField(max_length = 50, blank = True)
    date = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']