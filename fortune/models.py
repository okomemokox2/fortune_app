from django.db import models

class Fortune(models.Model):
    xnumber = models.IntegerField(default=1)
    messages = models.CharField(max_length=200, default='Default Message')
    ynumber = models.IntegerField(default=1)
    messages2 = models.CharField(max_length=200, default='Default Message')

    def __str__(self):
        return f"Fortune #{self.pk}"
