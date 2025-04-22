from django.db import models

# Create your models here.

class Student(models.Model):

    name=models.CharField(max_length=20)

    course=models.CharField(max_length=200)

    address=models.TextField()

    phone=models.CharField(max_length=12,unique=True)

    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name






