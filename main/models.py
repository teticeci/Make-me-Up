# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # menghubungankan relasi dari dua tabel
    name = models.CharField(max_length=255) # membuat text column dengan max length karakternya
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()