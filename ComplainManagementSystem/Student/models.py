from django.db import models

# Create your models here.


class Student(models.Model):

    user_name = models.CharField(max_length=100,unique=True,null=True)
    email = models.EmailField(blank=True)
    department = models.CharField(max_length=100,blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
