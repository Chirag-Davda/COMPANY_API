from django.db import models

# Create your models here.
#Creating company model
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=
                            (('IT','IT'),
                             ('Non IT','Non IT'),
                             ('Mobile Phones','Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
       return self.name + " " + self.location
   
# Employee Model
class Employee(models.Model):
    Employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=
                                (('Manager', 'Manager'),
                                 ('Software Developer', 'Software Developer'),
                                 ('Project Leader', 'Project Leader')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    