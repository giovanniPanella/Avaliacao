from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
