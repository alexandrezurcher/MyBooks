from django.db import models
from datetime import datetime


class Book(models.Model):
    book = models.TextField(max_length=255)
    ended = models.BooleanField(default=False) 
    resume = models.TextField(max_length=255)
    date = models.DateField(default=datetime.now)