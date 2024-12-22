from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    pin = models.CharField(max_length=13)
    age = models.IntegerField(null=True)
    department = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True, default="111")
    profile_pic = models.ImageField(upload_to='static/', null=True, blank=True)
    #image = pin +".jpg"

    def __str__(self):
        return str(self.name +" "+ self.pin)

class Post(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/posted_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
                        
    def __str__(self):
        return self.title

