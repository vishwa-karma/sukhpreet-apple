from django.conf import settings
from django.db import models


class Cluster(models.Model):
    cluster = models.CharField(max_length=200)
    servers = models.IntegerField(default=0)


    def __str__(self):
        return self.cluster