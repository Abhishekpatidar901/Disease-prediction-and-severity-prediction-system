from django.db import models

# Create your models here.
class details(models.Model):
    pid = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=200,default='')
    Sex=models.CharField(max_length=200,default='')
    Age=models.CharField(max_length=200,default='')
    Weight=models.CharField(max_length=200,default='')
    Disease=models.CharField(max_length=200,default='')
    Severity=models.CharField(max_length=200,default='')
    Per=models.FloatField()

class medicines(models.Model):
    # Fields for the 'second_db' database
    Disease=models.CharField(max_length=200,default='')
    Severity=models.CharField(max_length=200,default='')
    medic=models.CharField(max_length=700,default='')