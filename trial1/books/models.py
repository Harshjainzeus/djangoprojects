from django.db import models

# Create your models here.


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    class Meta :
        db_table = "zeus1"

class Author(models.Model):
    name = models.CharField(max_length=256)

#
# first_name = models.CharField('firstName', max_length=150, blank=True)
# email=models.EmailField('email Address', blank=True)