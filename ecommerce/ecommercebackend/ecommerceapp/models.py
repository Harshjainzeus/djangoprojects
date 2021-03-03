from django.db import models

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name


class Product(models.Model):
    title = models.CharField(max_length=256)
    department = models.ForeignKey(Department, related_name='product', on_delete=models.CASCADE)
    seller = models.CharField(max_length=120)
    cost = models.FloatField()
    image_url = models.CharField(max_length=500)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

