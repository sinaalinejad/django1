from django.db import models

# Create your models here.
class User(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    password_rep=models.CharField(max_length=50)
    def __str__(self):
        return self.lastname
class customer(models.Model):
    tell_num=models.IntegerField()
    address=models.CharField(max_length=50)
    baz_type=models.CharField(max_length=50,null=True)
    baz_num=models.IntegerField()
    price=models.CharField(max_length=50,null=True)