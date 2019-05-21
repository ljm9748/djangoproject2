from django.db import models

class Message(models.Model):
    content=models.TextField()
    writer=models.CharField(max_length=20)
    date=models.DateField()




