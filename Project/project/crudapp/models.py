from django.db import models

# Create your models here.
class Study(models.Model):
    sname=models.CharField(max_length=30)
    phase=models.TextField()
    sponsor=models.TextField()
    description=models.TextField()

    def __str__(self):
        return self.sname
