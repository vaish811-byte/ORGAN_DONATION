

# Create your models here.
from django.db import models
class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    organs = models.CharField(max_length=100)
    date_pledged = models.DateTimeField(auto_now_add=True, editable=False)
    

class Recipient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    required_organ = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=150)
    hospital_address = models.TextField()
    urgency_level = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    contact = models.CharField(max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



