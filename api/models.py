from django.db import models



class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    departament = models.CharField(max_length=25)
    salary = models.FloatField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    