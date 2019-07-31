from django.db import models

class Hblog(models.Model):

    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]