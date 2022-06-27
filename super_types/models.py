from django.db import models

# Created products class

class SuperType(models.Model):
    super_type = models.CharField(max_length=255)
    