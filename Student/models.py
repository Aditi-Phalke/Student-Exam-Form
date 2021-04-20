from django.db import models

# Create your models here.
class Contact(models.Model):
    usn=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100, default="")
    sem=models.CharField(max_length=10, default="")
    phone=models.CharField(max_length=30, default="")
    email=models.EmailField()


    def __str__(self):
        return self.name