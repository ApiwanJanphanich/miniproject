from django.db import models

# Create your models here.
class Person(models.Model):
    P_id = models.AutoField(primary_key=True)
    p_firstname = models.CharField(max_length=50,null=True)
    p_lastname = models.CharField(max_length=50,null=True)
    p_position = models.CharField(max_length=50,null=True)
    p_local = models.CharField(max_length=50,null=True)
    p_number = models.CharField(max_length=50,null=True)
    p_work = models.DateField(null=True)
    p_contract = models.CharField(max_length=50,null=True)
    p_salary = models.CharField(max_length=50,null=True)
    p_picture = models.ImageField(upload_to='profile_pictures/')
    def __str__(self):
        return f'{self.p_firstname} {self.p_firstname} {self.p_position}{self.p_local} {self.p_number} {self.p_work} {self.p_contract} {self.p_salary} '