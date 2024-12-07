from django.db import models

# Create your models here.
from django.db import models

class Appointment(models.Model):
    username = models.CharField(max_length=10)
    date = models.DateField()
    first_name = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} ({self.date})"
