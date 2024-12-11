from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    pin = models.CharField(max_length=13)
    age = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    #image = pin +".jpg"

    def __str__(self):
        return str(self.name +" "+ self.pin)
