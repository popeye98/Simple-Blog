from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Author(models.Model):
    sno=models.AutoField(primary_key=True)

    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Bio=models.TextField()
    Slug=models.CharField(max_length=30)
    Joined=models.DateTimeField(blank=True)
   # thumb = models.ImageField(default="keys.jpg", blank=True)
    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return  self.Name