from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    noOfGuest = models.SmallIntegerField()
    bookingDate = models.DateField()

    def __str__(self): 
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory = models.SmallIntegerField()

    def __str__(self): 
        return f'{self.title} : {str(self.price)}'