from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Name=models.CharField(max_length=200)
    Userid=models.EmailField()
    Number=models.IntegerField()
    Password=models.CharField(max_length=200)
    Con_password=models.CharField(max_length=200)
    class Meta:
        verbose_name= "Student"
        verbose_name_plural="Student"
        db_table="LoginData"
    
    def __str__(self):
        return self.Name