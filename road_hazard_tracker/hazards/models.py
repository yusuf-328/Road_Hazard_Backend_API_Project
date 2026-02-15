from django.db import models
from django.contrib.auth.models import User

class Hazard(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('resolved', 'Resolved')]
    SEVERITY_CHOICES = [(i, i) for i in range(1, 6)]

    title = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    severity = models.IntegerField(choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title