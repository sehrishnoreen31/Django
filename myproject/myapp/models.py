from django.db import models

# Create your models here.
class Employee(models.Model):
    empno = models.CharField(max_length=50)
    empname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    salary = models.IntegerField()
    joined_date = models.DateField(auto_now=True)
    class Meta:
        db_table = 'emplyee'

    def __str__(self):
        return self.empname
    