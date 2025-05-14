from django.db import models

class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    empn0 = models.CharField(max_length=50)
    empname = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)