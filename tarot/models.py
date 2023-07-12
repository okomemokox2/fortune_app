from django.db import models

class TarotCard(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
