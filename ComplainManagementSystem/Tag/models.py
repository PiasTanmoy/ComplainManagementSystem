from django.db import models
from Complain.models import Complain


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

class ComplainTag(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.complain)+':'+ str(self.tag.tag_name)