from django.db import models
from Student.models import Student
import datetime

# Create your models here.
class Complain(models.Model):
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=100, choices=(('1', 'Approved'), ('2', 'Not Approved'), ('3', 'Pending')), default='1')
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(('1', 'General'), ('2', 'Departmental'), ('3', 'Both')), default='1')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' : ' + self.student.user_name




