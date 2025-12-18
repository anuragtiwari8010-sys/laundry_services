from django.db import models


class Service(models.Model):
    service_title = models.CharField(max_length=150)
    service_desc = models.TextField()
    service_read_link = models.CharField(max_length=150)

    def __str__(self):
        return self.service_title


