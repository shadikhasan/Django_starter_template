from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now = True)

    
