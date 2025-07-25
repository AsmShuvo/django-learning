from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    # renames the instances of the model with their title name
    def __str__(self):
        return self.title