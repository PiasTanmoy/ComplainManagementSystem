from django.db import models
from Student.models import Student
import datetime

# Create your models here.
class Complain(models.Model):
    image = models.ImageField(upload_to='complain/image/', blank=True)
    status = models.CharField(max_length=100, choices=(('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Not Approved', 'Pending')), default='Approved')
    description = models.TextField()
    type = models.CharField(max_length=100, choices=(('General', 'General'), ('Departmental', 'Departmental'), ('Both', 'Both')), default='General')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' : ' + self.student.user_name


class Comment(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    description = models.TextField()

    def __str__(self):
        return str(self.complain.id) + ':' + self.student.user_name


class Vote(models.Model):
    complain = models.ForeignKey(Complain,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False,null=True)
    downvote = models.BooleanField(default=False,null=True)

    class Meta:
        unique_together = ('complain','student')

    def __str__(self):
        return str(self.complain.id) +' : '+self.student.user_name




