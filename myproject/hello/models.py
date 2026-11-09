from django.db import models

# Create your models here.

class Message(models.Model):
    message_text = models.CharField(max_length=250)
    date = models.DateTimeField('date created', auto_now_add=True)
    def __str__(self):
        return self.message_text