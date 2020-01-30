from django.db import models

# Create your models here.
class sale(models.Model):
    Gender = models.CharField(max_length=100)
    Age = models.IntegerField()
    EstimatedSalary = models.IntegerField()
    def to_dict(self):
        return {

            'Gender':self.Gender,
            'Age':self.Age,
            'EstimatedSalary':self.EstimatedSalary
        }
