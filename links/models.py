from django.db import models


# Create your models here.


class Director(models.Model):
    firstName = models.CharField(max_length= 200)
    lastName = models.CharField(max_length= 200)
    employmentNo = models.TextField()
    
    def __str__(self):
        return self.firstName

class SeniorManager(models.Model):
    director = models.ForeignKey(Director, null=True, blank = True,on_delete=models.CASCADE)
    firstName = models.CharField(max_length= 200)
    lastName = models.CharField(max_length= 200)
    employmentNo = models.TextField()
    
    def __str__(self):
        return self.firstName
    
class Manager(models.Model):
    seniorManager = models.ForeignKey(SeniorManager, null=True, blank = True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length= 200)
    lastName = models.CharField(max_length= 200)
    employmentNo = models.TextField()
    
    def __str__(self):
        return self.firstName

class SeniorDeveloper(models.Model):
    manager = models.ForeignKey(Manager, null=True, blank = True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length= 200)
    lastName = models.CharField(max_length= 200)
    employmentNo = models.TextField()
    
    def __str__(self):
        return self.firstName

class JuniorDeveloper(models.Model):
    seniorDeveloper = models.ForeignKey(SeniorDeveloper, null=True, blank = True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length= 200)
    lastName = models.CharField(max_length= 200)
    employmentNo = models.TextField()
    
    def __str__(self):
        return self.firstName

