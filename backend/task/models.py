from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']