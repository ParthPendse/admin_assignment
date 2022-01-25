from django.db import models

# Create your models here.
class Cricketer(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    position = models.CharField(max_length = 100)
    description = models.TextField()

    def __str__(self):
        result = self.name+" - "+self.position
        return result

    class Meta:
        db_table='cricketer'