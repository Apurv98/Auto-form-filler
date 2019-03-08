from django.db import models

# Create your models here.
class FormData(models.Model):
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
