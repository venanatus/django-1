from django.db import models

# Create your models here.
class Course(models.Model):
   title = models.CharField(max_length=255)
   description = models.TextField()
   price = models.IntegerField()
   duration = models.IntegerField()

   def __str__(self):
       return self.title
   
   
   
class Teacher(models.Model):
   full_name = models.CharField(max_length=255)
   teaching_course = models.CharField(max_length=255)

   def __str__(self):
       return self.full_name


class Application(models.Model):
    client_name = models.CharField('Имя',max_length=255)
    client_last_name = models.CharField('Фамилия', max_length=255, null=True)
    client_phone_number = models.CharField('Номер телефона',max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.client_name} {self.client_last_name} (+{self.client_phone_number})"
    
    