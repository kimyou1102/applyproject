from django.db import models

# Create your models here.
class Apply(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=4)
    gender = models.CharField(max_length=3)
    say = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
   