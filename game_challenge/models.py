from django.db import models

# Create your models here.
class Challenges(models.Model):
    
    name = models.CharField(max_length=100, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name