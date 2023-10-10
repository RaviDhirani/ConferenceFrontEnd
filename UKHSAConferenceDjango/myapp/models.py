from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Objectives(models.Model):
    objective = models.CharField(max_length=200)
    # specific = models.CharField(max_length=200)
    # measureable = models.CharField(max_length=200)
    # achievable = models.CharField(max_length=200)
    # relevant = models.CharField(max_length=200)
    # timely = models.CharField(max_length=200)
    complete =models.BooleanField(default=False)
