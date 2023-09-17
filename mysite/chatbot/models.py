from django.db import models

# Create your models here.
class Question(models.Model):
    content = models.TextField()
    response = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)