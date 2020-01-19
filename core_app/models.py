from django.db import models

# Create your models here.
class core_object(models.Model):
    name = models.CharField(max_length=200, null=True, unique=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    def __str__(self):
        return self.name + ' width: ' + self.width + ' height: ' + self.height + ' weight: ' + self.weight
