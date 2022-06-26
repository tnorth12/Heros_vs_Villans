from django.db import models

# Created products class

class SuperType(models.Model):
    type = models.CharField(max_length=255)
    