from django.db import models
from django.http import response
from django.test.client import Client

# Create your models here.

class Airplane(models.Model):
    code = models.CharField(max_length=64) 
    city = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.code}, {self.city} "

class Flights(models.Model):
    origin = models.ForeignKey(Airplane,on_delete=models.CASCADE,related_name="departure")
    destination = models.ForeignKey(Airplane,on_delete=models.CASCADE,related_name="arrival")
    duration = models.IntegerField() 
    def __str__(self):
        return f"{self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        return self.origin != self.destination or self.duration > 0
    
    def test_index(self):
        c = Client()
        response=c.get("/flights")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context["flights"].count(),3)
