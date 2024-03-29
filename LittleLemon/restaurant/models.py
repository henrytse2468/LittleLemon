from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory = models.SmallIntegerField()
    menu_item_description = models.TextField(max_length=1000, default='') 

    def __str__(self): 
        return f'{self.name} : {str(self.price)}'