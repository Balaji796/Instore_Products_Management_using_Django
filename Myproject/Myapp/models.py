from django.db import models

# Create your models here.
class stud(models.Model):
    Name=models.CharField(max_length=30, null=True)
    Piece_Kg=models.CharField(max_length=30, null=True)
    Type=models.CharField(max_length=30, null=True)
    Quantity=models.FloatField(max_length=30, null=True)
    Price=models.CharField(max_length=30, null=True)
class bill(models.Model):
    Name=models.CharField(max_length=30, null=True)
    quan=models.CharField(max_length=30, null=True)
    price=models.CharField(max_length=30, null=True)
    cash=models.CharField(max_length=30, null=True)
class customer(models.Model):
    date=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    addr=models.CharField(max_length=30)
    amount=models.CharField(max_length=30)
